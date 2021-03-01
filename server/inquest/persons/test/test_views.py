from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from nose.tools import eq_
from faker import Faker
import factory

from inquest.persons.models import Person
from inquest.persons.test.factories import PersonFactory
from inquest.persons.serializers import PersonSerializer

from inquest.users.test.factories import UserFactory

fake = Faker()


class TestPersonListTestCase(APITestCase):
    """ Tests /persons list operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("persons-list")
        self.person_data = factory.build(dict, FACTORY_CLASS=PersonFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.person_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        person = Person.objects.get(pk=response.data.get("id"))
        eq_(person.description, self.person_data.get("description"))

    def test_get_list_returns_only_my_persons(self):
        # Set testing persons
        PersonFactory(user_created=self.user)
        user2 = UserFactory()
        PersonFactory(user_created=user2)
        # Test response and results
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

        persons = Person.objects.filter(user_created=self.user)
        serializer = PersonSerializer(persons, many=True)
        eq_(response.data["count"], 1)
        eq_(response.data["results"], serializer.data)


class TestPersonDetailTestCase(APITestCase):
    """ Tests /persons detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.person = PersonFactory(user_created=self.user)
        self.url = reverse("comapnies-detail", kwargs={"pk": self.person.pk})

    def test_get_request_returns_a_given_person(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_person(self):
        new_description = fake.text()
        payload = {"description": new_description}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        person = Person.objects.get(pk=self.person.id)
        eq_(person.description, new_description)

    def test_put_request_updates_a_person(self):
        payload = factory.build(dict, FACTORY_CLASS=PersonFactory)
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        person = Person.objects.get(pk=self.person.id)
        eq_(person.description, payload["description"])

    def test_set_person_completed(self):
        custom_action = reverse("person-set-completed", kwargs={"pk": self.person.pk})
        response = self.client.post(custom_action)
        eq_(response.status_code, status.HTTP_200_OK)

        person = Person.objects.get(pk=self.person.id)
        eq_(person.is_completed, True)

    def test_delete_request_deletes_a_person(self):
        response = self.client.delete(self.url)
        eq_(response.status_code, status.HTTP_204_NO_CONTENT)

        person = Person.objects.filter(pk=self.person.id).first()
        eq_(person, None)
