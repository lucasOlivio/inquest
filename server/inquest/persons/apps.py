from django.apps import AppConfig


class PersonsConfig(AppConfig):
    """ App configuration for persons app. """

    name = "inquest.persons"
    verbose_name = "Person"

    def ready(self):
        try:
            import inquest.persons.signals  # noqa F401
        except ImportError:
            pass
