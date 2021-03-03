from fordev.validator import cnpj
from rest_framework.serializers import ValidationError


def validate_cnpj(doc):
    if not cnpj(doc):
        raise ValidationError("CNPJ inválido!")
    return doc
