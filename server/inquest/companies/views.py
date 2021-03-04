from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from inquest.companies.mixins import ManageOwnersMixin
from inquest.companies.models import Company
from inquest.companies.serializers import CompanySerializer
from inquest.permissions import IsOwnerOrAdmin


class CompanyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    ManageOwnersMixin,
    viewsets.GenericViewSet,
):
    """ Creates, updates, deletes, retrieves companies and add or removes owners. """

    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Company.objects.filter(user_created=self.request.user)
        return Company.objects.all()

    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
