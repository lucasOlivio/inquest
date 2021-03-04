from rest_framework import serializers


class DefaultFieldsSerializer(serializers.ModelSerializer):
    """ Default serializer to update and set default fields. """

    user_created = serializers.StringRelatedField()
    user_updated = serializers.StringRelatedField()

    def update(self, instance, valid_data):
        """ Set default user updated for current user. """
        valid_data["user_updated"] = self.context["request"].user
        return super().update(instance, valid_data)

    def create(self, valid_data):
        """ Set default user created for current user. """
        valid_data["user_created"] = self.context["request"].user
        valid_data["user_updated"] = self.context["request"].user
        return self.Meta.model.objects.create(**valid_data)

    class Meta:
        abstract = True
        fields = (
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
        )
        read_only_fields = (
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
        )
