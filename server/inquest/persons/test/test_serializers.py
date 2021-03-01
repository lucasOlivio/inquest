from django.test import TestCase
from django.forms.models import model_to_dict

from inquest.persons.test.factories import PersonFactory
from inquest.persons.serializers import PersonSerializer

from nose.tools import eq_, ok_
import pytest

pytestmark = pytest.mark.django_db


class TestCreatePersonSerializer(TestCase):
    def setUp(self):
        self.person_data = model_to_dict(PersonFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = PersonSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = PersonSerializer(data=self.person_data)
        ok_(serializer.is_valid())
