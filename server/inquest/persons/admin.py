from django.contrib import admin
from inquest.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "is_completed",
        "date_completed",
        "delivery_address",
        "delivery_name",
        "cellphone",
        "email",
        "user_created",
        "date_created",
        "user_updated",
        "date_updated",
    )
    list_filter = ("is_completed", "date_completed", "date_created", "date_updated")
    search_fields = (
        "description",
        "delivery_name",
        "delivery_state",
        "delivery_city",
        "delivery_street",
        "delivery_number",
        "delivery_complement",
        "delivery_cep",
        "cellphone",
        "email",
        "user_created__username",
        "user_updated__username",
    )
