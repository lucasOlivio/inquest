from rest_framework import serializers

from inquest.companies.models import Company
from inquest.companies.validators import validate_cnpj
from inquest.serializers import DefaultFieldsSerializer


class CompanySerializer(DefaultFieldsSerializer):
    """ Serializer to create, list, update and delete companies. """

    company_name = serializers.CharField(max_length=255)
    fantasy_name = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=2)
    cnpj = serializers.CharField(
        max_length=18,
        validators=[validate_cnpj],
    )
    companies_owned = serializers.StringRelatedField(many=True, read_only=True)
    physical_owners = serializers.StringRelatedField(many=True, read_only=True)
    legal_owners = serializers.StringRelatedField(many=True, read_only=True)

    class Meta(DefaultFieldsSerializer.Meta):
        model = Company
        fields = (
            "id",
            "company_name",
            "fantasy_name",
            "state",
            "cnpj",
            "companies_owned",
            "physical_owners",
            "legal_owners",
        ) + DefaultFieldsSerializer.Meta.fields
        read_only_fields = (
            "companies_owned",
            "physical_owners",
            "legal_owners",
        ) + DefaultFieldsSerializer.Meta.read_only_fields
