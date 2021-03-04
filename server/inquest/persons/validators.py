from fordev.validator import cpf
from rest_framework.serializers import ValidationError


def validate_cpf(doc):
    """Basic function to validate the CPF number for serializer field

    Args:
        doc (str): The CPF number, accepts with or without characters

    Raises:
        ValidationError: CPF inválido!

    Returns:
        doc: The CPF number
    """
    if not cpf(doc):
        raise ValidationError("CPF inválido!")
    return doc
