import factory

from inquest.persons.test.factories import PersonFactory
from inquest.users.test.factories import UserFactory


class OwnershipFactory(factory.django.DjangoModelFactory):

    name = factory.Faker("name")
    value = 11.11
    owner = factory.SubFactory(PersonFactory)
    user_created = factory.SubFactory(UserFactory)

    class Meta:
        model = "ownerships.Ownership"
