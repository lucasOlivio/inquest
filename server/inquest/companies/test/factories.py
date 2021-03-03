import factory
from fordev.generator import cnpj, uf

from inquest.users.test.factories import UserFactory


class CompanyFactory(factory.django.DjangoModelFactory):

    company_name = factory.Faker("name")
    fantasy_name = factory.Faker("name")
    state = uf(n=1)[0]
    cnpj = cnpj(formatting=True)
    user_created = factory.SubFactory(UserFactory)

    class Meta:
        model = "companies.Company"
