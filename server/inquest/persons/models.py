from django.db import models
from django.utils import timezone

from inquest.users.models import User


class Person(models.Model):
    """ Class for physical persons and legal persons model. """

    name = models.CharField(
        verbose_name="Nome",
        max_length=255,
        help_text="Nome da pessoa.",
    )
    cpf = models.CharField(
        verbose_name="Nº CPF",
        max_length=14,
        help_text="Nº do CPF da pessoa.",
    )
    user_created = models.ForeignKey(
        User,
        verbose_name="Criado por",
        on_delete=models.DO_NOTHING,
        related_name="persons_created",
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
        related_name="persons_updated",
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
        return f'{self.name} - {self.cpf}'

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
