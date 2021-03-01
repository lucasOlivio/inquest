from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def type_user(self):
        """ Get label for user type """
        return "Administrador" if self.is_superuser else "Anunciante"

    def __str__(self):
        return self.username
