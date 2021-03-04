import factory
from django.urls import reverse
from nose.tools import eq_
from rest_framework import status
from rest_framework.test import APITestCase

from inquest.ownerships.models import Ownership
from inquest.ownerships.serializers import OwnershipSerializer
from inquest.ownerships.test.factories import OwnershipFactory
from inquest.persons.test.factories import PersonFactory
from inquest.users.test.factories import UserFactory


class TestOwnershipListTestCase(APITestCase):
    """ Tests /ownerships list operations. """

    def setUp(self):
        self.user = UserFactory()
        self.person = PersonFactory()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("ownerships-list")
        self.ownership_data = factory.build(dict, FACTORY_CLASS=OwnershipFactory)
        self.ownership_data["owner"] = self.person.pk

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.ownership_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        ownership = Ownership.objects.get(pk=response.data.get("id"))
        eq_(ownership.name, self.ownership_data.get("name"))

    def test_get_list_returns_only_my_created_ownerships(self):
        # Set testing ownerships
        OwnershipFactory(owner=self.person, user_created=self.user)
        user2 = UserFactory()
        OwnershipFactory(owner=self.person, user_created=user2)
        # Test response and results
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

        ownerships = Ownership.objects.filter(owner=self.person, user_created=self.user)
        serializer = OwnershipSerializer(ownerships, many=True)
        eq_(response.data["count"], 1)
        eq_(response.data["results"], serializer.data)


class TestOwnershipDetailTestCase(APITestCase):
    """ Tests /ownerships detail operations. """

    def setUp(self):
        self.user = UserFactory()
        self.person = PersonFactory()
        self.client.force_authenticate(user=self.user)
        self.ownership = OwnershipFactory(owner=self.person, user_created=self.user)
        self.url = reverse("ownerships-detail", kwargs={"pk": self.ownership.pk})

    def test_get_request_returns_a_given_ownership(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_ownership(self):
        new_value = 77.7
        payload = {"value": new_value}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        ownership = Ownership.objects.get(pk=self.ownership.id)
        eq_(ownership.value, new_value)

    def test_put_request_updates_a_ownership(self):
        payload = factory.build(dict, FACTORY_CLASS=OwnershipFactory)
        payload["owner"] = self.person.pk
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        ownership = Ownership.objects.get(pk=self.ownership.id)
        eq_(ownership.name, payload["name"])

    def test_delete_request_deletes_a_ownership(self):
        response = self.client.delete(self.url)
        eq_(response.status_code, status.HTTP_204_NO_CONTENT)

        ownership = Ownership.objects.filter(pk=self.ownership.id).first()
        eq_(ownership, None)
