from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from inquest.permissions import IsOwnerOrAdmin
from inquest.persons.models import Person
from inquest.persons.serializers import PersonSerializer


class PersonViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """ Creates, updates, deletes and retrieves persons. """

    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Person.objects.filter(user_created=self.request.user)
        return Person.objects.all()

    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
