from django.db import models
from django.utils import timezone

from inquest.users.models import User


class Person(models.Model):
    """ Class for physical persons and legal persons model. """

    description = models.CharField(
        verbose_name="Descrição",
        max_length=255,
        help_text="Descrição da peça que está sendo solicitada.",
    )
    is_completed = models.BooleanField(
        verbose_name="Finalizada",
        default=False,
        help_text="Status de finalização da entrega.",
    )

    delivery_state = models.CharField(
        verbose_name="Estado", max_length=255, help_text="Estado de entrega."
    )
    delivery_city = models.CharField(
        verbose_name="Cidade", max_length=255, help_text="Cidade de entrega."
    )
    delivery_street = models.CharField(
        verbose_name="Endereço", max_length=255, help_text="Endereço de entrega."
    )
    delivery_number = models.IntegerField(
        verbose_name="Número", help_text="Número de entrega."
    )
    delivery_complement = models.CharField(
        verbose_name="Complemento",
        max_length=255,
        null=True,
        blank=True,
        help_text="Complemento de entrega.",
    )
    delivery_cep = models.CharField(
        verbose_name="CEP", max_length=8, help_text="CEP de entrega."
    )
    delivery_name = models.CharField(
        verbose_name="Nome destinatário",
        max_length=255,
        help_text="Nome da pessoa que receberá a entrega.",
    )

    cellphone = models.CharField(
        verbose_name="Celular",
        default="",
        blank=True,
        max_length=15,
        help_text="Celular do destinatário para contato.",
    )
    email = models.CharField(
        verbose_name="Email",
        default="",
        blank=True,
        max_length=255,
        help_text="Email do destinatário para contato.",
    )

    user_created = models.ForeignKey(
        User,
        verbose_name="Criador",
        related_name="persons",
        on_delete=models.CASCADE,
        help_text="Criador da empresa.",
    )
    date_created = models.DateTimeField(
        verbose_name="Data de criação", default=timezone.now
    )
    user_updated = models.ForeignKey(
        User,
        verbose_name="Ultimo atualizador",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="Último usuário que atualizou a empresa.",
    )
    date_updated = models.DateTimeField(
        verbose_name="Data da atualização",
        default=timezone.now,
        help_text="Data da ultima atualização da empresa.",
    )
    date_completed = models.DateTimeField(
        verbose_name="Data de finalização",
        null=True,
        blank=True,
        help_text="Data que a empresa foi finalizada.",
    )

    def delivery_address(self):
        return f"{self.delivery_street}, {self.delivery_number},\
             {self.delivery_complement}, {self.delivery_city},\
             {self.delivery_state} - {self.delivery_cep}"

    def __str__(self):
        return f'{self.description} - \
            { "Aberta" if not self.is_completed else "Finalizada"}'

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
