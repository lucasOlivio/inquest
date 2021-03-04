from django.contrib import admin

from inquest.persons.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """ Custom admin panel configuration for Person model. """

    exclude = ("user_created", "user_updated")
    list_display = (
        "name",
        "cpf",
        "user_created",
        "date_created",
        "user_updated",
        "date_updated",
    )
    list_filter = ("date_created", "date_updated")
    search_fields = ("name", "cpf", "user_created__username", "user_updated__username")
