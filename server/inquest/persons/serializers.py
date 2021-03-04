from rest_framework import serializers

from inquest.persons.models import Person
from inquest.persons.validators import validate_cpf


class PersonSerializer(serializers.ModelSerializer):
    """ Serializer to create, list, update and delete persons """

    name = serializers.CharField(max_length=255)
    cpf = serializers.CharField(
        max_length=14,
        validators=[validate_cpf],
    )
    companies_owned = serializers.StringRelatedField(many=True)
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
        return Person.objects.create(**valid_data)

    class Meta:
        model = Person
        fields = (
            "id",
            "name",
            "cpf",
            "companies_owned",
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
        )
        read_only_fields = (
            "companies_owned",
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
        )
