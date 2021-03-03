import pytest
from django.forms.models import model_to_dict
from django.test import TestCase
from nose.tools import eq_, ok_

from inquest.companies.serializers import CompanySerializer
from inquest.companies.test.factories import CompanyFactory

pytestmark = pytest.mark.django_db


class TestCreateCompanySerializer(TestCase):
    def setUp(self):
        self.company_data = model_to_dict(CompanyFactory.build())
        self.company_data["cnpj"] = self.company_data["_cnpj"]

    def test_serializer_with_empty_data(self):
        serializer = CompanySerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CompanySerializer(data=self.company_data)
        ok_(serializer.is_valid())
