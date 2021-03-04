import re

from django.shortcuts import get_object_or_404
from fordev.validator import cnpj, cpf
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from inquest.companies.models import Company
from inquest.persons.models import Person


class ManageOwnersMixin(object):
    """ Add or remove owners from companies accordingly to owner's type """

    @action(detail=True, methods=["post"])
    def add_owner(self, request, pk=None):
        instance = self.get_object()
        doc = request.data.get("doc", None)
        doc = re.sub("[^0-9]", "", doc)
        if cpf(doc):
            person = get_object_or_404(Person, _cpf=doc)
            instance.physical_owners.add(person)
        elif cnpj(doc):
            company = get_object_or_404(Company, _cnpj=doc)
            instance.legal_owners.add(company)
        else:
            return Response(
                "Nª de documento inválido!", status=status.HTTP_400_BAD_REQUEST
            )
        return Response("OK", status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["delete"])
    def remove_owner(self, request, pk=None):
        instance = self.get_object()
        doc = request.data.get("doc", None)
        doc = re.sub("[^0-9]", "", doc)
        if cpf(doc):
            person = get_object_or_404(Person, _cpf=doc)
            instance.physical_owners.remove(person)
        elif cnpj(doc):
            Company.objects.filter(_cnpj=doc)
            company = get_object_or_404(Company, _cnpj=doc)
            instance.legal_owners.remove(company)
        else:
            return Response(
                "Nª de documento inválido!", status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
