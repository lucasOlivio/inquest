from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = "inquest.companies"
    verbose_name = "Company"

    def ready(self):
        try:
            import inquest.companies.signals  # noqa F401
        except ImportError:
            pass
