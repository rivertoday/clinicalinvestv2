__author__ = 'jeremyjiang'
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the user.
        return obj == request.user


class CheckOperationPerm(permissions.BasePermission):# for details
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to SAFE request with granted permission,
        # print(obj)
        return obj == request.user
        # if request.method in permissions.SAFE_METHODS:
        #     if request.user.has_perm('myusers.user_operation'):
        #         return True
        #     else:
        #         return False
        #
        # else:
        #     if request.user.has_perm('myusers.user_operation'):
        #         # Write permissions are only allowed to the owner of the GeneralInfo.
        #         return obj.email == request.user
