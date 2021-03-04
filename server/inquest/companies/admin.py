from django.contrib import admin

from inquest.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Custom admin panel configuration for Company model. """

    exclude = ("user_created", "user_updated")
    list_display = (
        "company_name",
        "fantasy_name",
        "state",
        "cnpj",
        "user_created",
        "date_created",
        "user_updated",
        "date_updated",
    )
    list_filter = ("date_created", "date_updated", "state")
    search_fields = (
        "company_name",
        "fantasy_name",
        "state",
        "cnpj",
        "user_created__username",
        "user_updated__username",
    )
