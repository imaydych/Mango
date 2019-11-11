from rest_framework import permissions


class IsCurrentUserOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
        # # Read permissions are allowed to any request,
        # # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     # The method is a safe method
        #     return True
        # else:
        #     # The method isn't a safe method
        #     # Only owners are granted permissions for unsafe methods
        #     return obj.owner == request.user
