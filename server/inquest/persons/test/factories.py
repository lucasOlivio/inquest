from inquest.users.test.factories import UserFactory

import factory

from validate_docbr import CPF


class PersonFactory(factory.django.DjangoModelFactory):

    name = factory.Faker("name")
    cpf = CPF().generate()
    user_created = factory.SubFactory(UserFactory)

    class Meta:
        model = "persons.Person"
