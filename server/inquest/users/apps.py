from django.apps import AppConfig


class UsersConfig(AppConfig):
    """ App configuration for users app. """

    name = "inquest.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import inquest.users.signals  # noqa F401
        except ImportError:
            pass
