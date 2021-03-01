from django.utils import timezone

from rest_framework import serializers

from inquest.persons.models import Person


class PersonSerializer(serializers.ModelSerializer):
    """ Serializer to create, list, update and delete persons """

    user_created = serializers.StringRelatedField()
    user_updated = serializers.StringRelatedField()

    def update(self, instance, valid_data):
        """ Set default user updated for current user and updated date """
        valid_data["user_updated"] = self.context["request"].user
        valid_data["date_updated"] = timezone.now()
        return super().update(instance, valid_data)

    def create(self, valid_data):
        """ Set default user created for current user """
        valid_data["user_created"] = self.context["request"].user
        return Person.objects.create(**valid_data)

    def set_completed(self, instance):
        if instance.is_completed:
            return False

        valid_data = {"is_completed": True, "date_completed": timezone.now()}
        return super().update(instance, valid_data)

    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = (
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
            "is_completed",
            "date_completed",
        )
