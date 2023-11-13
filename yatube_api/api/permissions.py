from rest_framework import permissions


class IsAuthenticatedAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Permission to only allow owner of an object to change it."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
