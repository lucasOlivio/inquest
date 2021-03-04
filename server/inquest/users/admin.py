from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """ Custom admin panel configuration for User model. """

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "date_joined",
    )
    list_filter = ("is_active", "date_joined", "is_superuser")
    search_fields = ("username", "email", "first_name", "last_name")
