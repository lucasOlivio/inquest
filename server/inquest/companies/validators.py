from fordev.validator import cnpj
from rest_framework.serializers import ValidationError


def validate_cnpj(doc):
    """Basic function to validate the CNPJ number for serializer field

    Args:
        doc (str): The CNPJ number, accepts with or without characters

    Raises:
        ValidationError: CNPJ inválido!

    Returns:
        doc: The CNPJ number
    """
    if not cnpj(doc):
        raise ValidationError("CNPJ inválido!")
    return doc
