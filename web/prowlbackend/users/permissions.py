from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed users with same token
        return obj.auth_token == request.user.auth_token
