from django.apps import AppConfig


class OwnershipsConfig(AppConfig):
    """ App configuration for ownerships app. """

    name = "inquest.ownerships"
    verbose_name = "Ownership"

    def ready(self):
        try:
            import inquest.ownerships.signals  # noqa F401
        except ImportError:
            pass
