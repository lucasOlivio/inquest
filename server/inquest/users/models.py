from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Extends from AbstractUser model in case custom fields or methods need to be added. """

    def __str__(self):
        return self.username
