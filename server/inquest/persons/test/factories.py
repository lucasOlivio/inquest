import factory
from fordev.generator import cpf

from inquest.users.test.factories import UserFactory


class PersonFactory(factory.django.DjangoModelFactory):

    name = factory.Faker("name")
    cpf = cpf(formatting=True)
    user_created = factory.SubFactory(UserFactory)

    class Meta:
        model = "persons.Person"
