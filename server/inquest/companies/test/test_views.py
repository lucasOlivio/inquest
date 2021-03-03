import factory
from django.urls import reverse
from fordev.generator import cnpj
from nose.tools import eq_
from rest_framework import status
from rest_framework.test import APITestCase

from inquest.companies.models import Company
from inquest.companies.serializers import CompanySerializer
from inquest.companies.test.factories import CompanyFactory
from inquest.persons.test.factories import PersonFactory
from inquest.users.test.factories import UserFactory


class TestCompanyListTestCase(APITestCase):
    """Tests /companies list operations."""

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("companies-list")
        self.company_data = factory.build(dict, FACTORY_CLASS=CompanyFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.company_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.get(pk=response.data.get("id"))
        eq_(company.cnpj, self.company_data.get("cnpj"))

    def test_get_list_returns_only_my_companies(self):
        # Set testing companies
        CompanyFactory(user_created=self.user)
        user2 = UserFactory()
        CompanyFactory(cnpj=cnpj(formatting=True), user_created=user2)
        # Test response and results
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

        companies = Company.objects.filter(user_created=self.user)
        serializer = CompanySerializer(companies, many=True)
        eq_(response.data["count"], 1)
        eq_(response.data["results"], serializer.data)


class TestCompanyDetailTestCase(APITestCase):
    """Tests /companies detail operations."""

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.company = CompanyFactory(user_created=self.user)
        self.company2 = CompanyFactory(
            cnpj=cnpj(formatting=True), user_created=self.user
        )
        self.person = PersonFactory(user_created=self.user)
        self.url = reverse("companies-detail", kwargs={"pk": self.company.pk})

    def test_get_request_returns_a_given_company(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_company(self):
        new_cnpj = cnpj(formatting=True)
        payload = {"cnpj": new_cnpj}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(pk=self.company.id)
        eq_(company.cnpj, new_cnpj)

    def test_put_request_updates_a_company(self):
        payload = factory.build(dict, FACTORY_CLASS=CompanyFactory)
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(pk=self.company.id)
        eq_(company.cnpj, payload["cnpj"])

    def test_add_owners(self):
        # Add legal owner
        custom_action = reverse("companies-add-owner", kwargs={"pk": self.company.pk})
        data = {"doc": self.company2.cnpj}
        response = self.client.post(custom_action, data=data)
        eq_(response.status_code, status.HTTP_201_CREATED)
        # Add physical owner
        data["doc"] = self.person.cpf
        response = self.client.post(custom_action, data=data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.get(pk=self.company.id)
        eq_(company.legal_owners.count(), 1)
        eq_(company.physical_owners.count(), 1)

    def test_remove_owners(self):
        # Remove legal owner
        custom_action = reverse(
            "companies-remove-owner", kwargs={"pk": self.company.pk}
        )
        data = {"doc": self.company2.cnpj}
        response = self.client.post(custom_action, data=data)
        eq_(response.status_code, status.HTTP_200_OK)
        # Add physical owner
        data["doc"] = self.person.cpf
        response = self.client.post(custom_action, data=data)
        eq_(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(pk=self.company.id)
        eq_(company.legal_owners.count(), 0)
        eq_(company.physical_owners.count(), 0)

    def test_delete_request_deletes_a_company(self):
        response = self.client.delete(self.url)
        eq_(response.status_code, status.HTTP_204_NO_CONTENT)

        company = Company.objects.filter(pk=self.company.id).first()
        eq_(company, None)
