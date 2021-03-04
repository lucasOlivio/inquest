from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """ Object-level permission to only allow the user edit itself or else just allow read mode. """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
