from rest_framework import serializers

from inquest.ownerships.models import Ownership
from inquest.persons.models import Person
from inquest.serializers import DefaultFieldsSerializer


class OwnershipSerializer(DefaultFieldsSerializer):
    """ Serializer to create, list, update and delete person's ownerships. """

    name = serializers.CharField(max_length=255)
    value = serializers.FloatField(required=False)
    owner = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())

    class Meta(DefaultFieldsSerializer.Meta):
        model = Ownership
        fields = (
            "id",
            "name",
            "value",
            "owner",
        ) + DefaultFieldsSerializer.Meta.fields
        read_only_fields = DefaultFieldsSerializer.Meta.read_only_fields
