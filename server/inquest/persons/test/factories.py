from inquest.users.test.factories import UserFactory

import factory


class PersonFactory(factory.django.DjangoModelFactory):

    description = factory.Faker("text")
    is_completed = False
    delivery_state = factory.Faker("text")
    delivery_city = factory.Faker("text")
    delivery_street = factory.Faker("text")
    delivery_number = factory.Faker("random_number")
    delivery_complement = factory.Faker("text")
    delivery_cep = "12345678"
    delivery_name = factory.Faker("name")
    cellphone = "123456789"
    email = factory.Faker("email")
    user_created = factory.SubFactory(UserFactory)

    class Meta:
        model = "persons.Person"
