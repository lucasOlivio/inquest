import factory


class UserFactory(factory.django.DjangoModelFactory):
    """ Generates an new User object for testing purposes. """

    username = factory.Sequence(lambda n: f"testuser{n}")
    password = factory.Faker(
        "password",
        length=10,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_active = True
    is_superuser = False

    class Meta:
        model = "users.User"
        django_get_or_create = ("username",)
