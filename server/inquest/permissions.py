from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or admins to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True
        return obj.user_created.pk == request.user.pk
