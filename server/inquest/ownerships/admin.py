from django.contrib import admin

from inquest.ownerships.models import Ownership


@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    exclude = ("user_created", "user_updated")
    list_display = (
        "name",
        "value",
        "owner",
        "user_created",
        "date_created",
        "user_updated",
        "date_updated",
    )
    list_filter = ("date_created", "date_updated")
    search_fields = (
        "name",
        "value",
        "owner",
        "user_created__username",
        "user_updated__username",
    )
