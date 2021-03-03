import re

from django.db import models

from inquest.users.models import User


class Person(models.Model):
    """ Class for physical persons model. """

    name = models.CharField(
        verbose_name="Nome",
        max_length=255,
        help_text="Nome da pessoa.",
        null=False,
        blank=False,
    )
    _cpf = models.CharField(
        verbose_name="Nº CPF",
        max_length=11,
        help_text="Nº do CPF da pessoa.",
        unique=True,
        null=False,
        blank=False,
        db_column="cpf",
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
        return self.name

    @property
    def cpf(self):
        return f"{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:11]}"

    @cpf.setter
    def cpf(self, val):
        self._cpf = re.sub("[^0-9]", "", val)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
