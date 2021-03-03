from fordev.validator import cpf
from rest_framework.serializers import ValidationError


def validate_cpf(doc):
    if not cpf(doc):
        raise ValidationError("CPF inválido!")
    return doc
