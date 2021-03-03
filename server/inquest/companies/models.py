import re

from django.db import models

from inquest.persons.models import Person
from inquest.users.models import User


class Company(models.Model):
    """ Class for company model. """

    company_name = models.CharField(
        verbose_name="Razão social",
        max_length=255,
        help_text="Razão social da empresa.",
        null=False,
        blank=False,
    )
    fantasy_name = models.CharField(
        verbose_name="Nome fantasia",
        max_length=255,
        help_text="Nome fantasia da empresa.",
        null=False,
        blank=False,
    )
    state = models.CharField(
        verbose_name="Estado",
        max_length=2,
        help_text="Sigla do estado da empresa.",
        null=False,
        blank=False,
    )
    _cnpj = models.CharField(
        verbose_name="Nº CNPJ",
        max_length=14,
        help_text="Nº do CNPJ da empresa.",
        unique=True,
        null=False,
        blank=False,
        db_column="cnpj",
    )
    physical_owners = models.ManyToManyField(
        Person, verbose_name="Donos pessoas físicas", related_name="companies_owned"
    )
    legal_owners = models.ManyToManyField(
        "Company",
        verbose_name="Donos pessoas jurídicas",
        related_name="companies_owned",
    )
    user_created = models.ForeignKey(
        User,
        verbose_name="Criado por",
        on_delete=models.DO_NOTHING,
        related_name="companies_created",
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
        related_name="companies_updated",
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
        return self.company_name

    @property
    def cnpj(self):
        return f"{self._cnpj[:2]}.{self._cnpj[2:5]}.{self._cnpj[5:8]}/{self._cnpj[8:12]}-{self._cnpj[12:14]}"

    @cnpj.setter
    def cnpj(self, val):
        self._cnpj = re.sub("[^0-9]", "", val)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
