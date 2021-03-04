from rest_framework import serializers

from inquest.companies.models import Company
from inquest.companies.validators import validate_cnpj


class CompanySerializer(serializers.ModelSerializer):
    """ Serializer to create, list, update and delete companies. """

    company_name = serializers.CharField(max_length=255)
    fantasy_name = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=2)
    cnpj = serializers.CharField(
        max_length=18,
        validators=[validate_cnpj],
    )
    companies_owned = serializers.StringRelatedField(many=True)
    physical_owners = serializers.StringRelatedField(many=True)
    legal_owners = serializers.StringRelatedField(many=True)
    user_created = serializers.StringRelatedField()
    user_updated = serializers.StringRelatedField()

    def update(self, instance, valid_data):
        """ Set default user updated for current user """
        valid_data["user_updated"] = self.context["request"].user
        return super().update(instance, valid_data)

    def create(self, valid_data):
        """ Set default user created for current user """
        valid_data["user_created"] = self.context["request"].user
        valid_data["user_updated"] = self.context["request"].user
        return Company.objects.create(**valid_data)

    class Meta:
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
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
        )
        read_only_fields = (
            "companies_owned",
            "physical_owners",
            "legal_owners",
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
        )
