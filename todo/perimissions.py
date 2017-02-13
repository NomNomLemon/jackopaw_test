from rest_framework.permissions import BasePermission


class OwnTaskPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method == 'GET':
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user
