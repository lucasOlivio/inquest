from rest_framework.serializers import ValidationError

from validate_docbr import CPF


def validate_cpf(cpf):
    validator = CPF()
    if not validator.validate(cpf):
        raise ValidationError("CPF inválido!")
    return cpf
