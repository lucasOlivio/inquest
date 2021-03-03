from django.utils import timezone

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from inquest.persons.models import Person
from inquest.persons.validators import validate_cpf

import re


class PersonSerializer(serializers.ModelSerializer):
    """ Serializer to create, list, update and delete persons """

    name = serializers.CharField(max_length=255)
    cpf = serializers.CharField(max_length=14, validators=[UniqueValidator(queryset=Person.objects.all()), validate_cpf])
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

    def to_internal_value(self, data):
        new_data = data.copy()
        if "cpf" in new_data:
            new_data["cpf"] = re.sub("[^0-9]", "", new_data["cpf"])

        return super(PersonSerializer, self).to_internal_value(new_data)

    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = (
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
        )
