from django.apps import AppConfig


class PersonsConfig(AppConfig):
    name = "inquest.persons"
    verbose_name = "Person"

    def ready(self):
        try:
            import inquest.persons.signals  # noqa F401
        except ImportError:
            pass
