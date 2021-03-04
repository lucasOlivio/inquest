from django.apps import AppConfig


class OwnershipsConfig(AppConfig):
    name = "inquest.ownerships"
    verbose_name = "Ownership"

    def ready(self):
        try:
            import inquest.ownerships.signals  # noqa F401
        except ImportError:
            pass
