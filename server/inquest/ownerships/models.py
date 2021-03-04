from django.db import models

from inquest.persons.models import Person
from inquest.users.models import User


class Ownership(models.Model):
    """ Class for ownerships model. """

    name = models.CharField(
        verbose_name="Nome",
        max_length=255,
        help_text="Nome da posse.",
        null=False,
        blank=False,
    )
    value = models.FloatField(
        verbose_name="Valor", help_text="Valor total da posse.", default=0
    )
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Proprietário",
        related_name="ownerships",
        blank=False,
        null=False,
    )
    user_created = models.ForeignKey(
        User,
        verbose_name="Criado por",
        on_delete=models.DO_NOTHING,
        related_name="ownerships_created",
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField(
        "Criado em", auto_now=False, auto_now_add=True, help_text="Criado em"
    )
    user_updated = models.ForeignKey(
        User,
        verbose_name="Atualizado por",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="ownerships_updated",
    )
    date_updated = models.DateTimeField(
        "Atualizado em",
        auto_now=True,
        auto_now_add=False,
        help_text="Atualizado em",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Posse"
        verbose_name_plural = "Posses"
