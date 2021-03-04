import pytest
from django.forms.models import model_to_dict
from django.test import TestCase
from nose.tools import eq_, ok_

from inquest.ownerships.serializers import OwnershipSerializer
from inquest.ownerships.test.factories import OwnershipFactory
from inquest.persons.test.factories import PersonFactory

pytestmark = pytest.mark.django_db


class TestCreateOwnershipSerializer(TestCase):
    """ Tests OwnershipSerializer creation and functions. """

    def setUp(self):
        self.person = PersonFactory()
        self.ownership_data = model_to_dict(OwnershipFactory.build(owner=self.person))

    def test_serializer_with_empty_data(self):
        serializer = OwnershipSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = OwnershipSerializer(data=self.ownership_data)
        ok_(serializer.is_valid())
