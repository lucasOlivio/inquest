from rest_framework import serializers

from inquest.persons.models import Person
from inquest.persons.validators import validate_cpf
from inquest.serializers import DefaultFieldsSerializer


class PersonSerializer(DefaultFieldsSerializer):
    """ Serializer to create, list, update and delete persons. """

    name = serializers.CharField(max_length=255)
    cpf = serializers.CharField(
        max_length=14,
        validators=[validate_cpf],
    )
    ownerships = serializers.StringRelatedField(many=True, read_only=True)
    companies_owned = serializers.StringRelatedField(many=True, read_only=True)

    class Meta(DefaultFieldsSerializer.Meta):
        model = Person
        fields = (
            "id",
            "name",
            "cpf",
            "ownerships",
            "companies_owned",
        ) + DefaultFieldsSerializer.Meta.fields
        read_only_fields = (
            "ownerships",
            "companies_owned",
        ) + DefaultFieldsSerializer.Meta.read_only_fields
