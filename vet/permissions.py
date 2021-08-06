from rest_framework.permissions import BasePermission


class OnlyAdminCanCreate(BasePermission):
    def has_permission(self, request, view):

        http_verb = request.method

        if http_verb == "POST" and request.user.is_staff:
            return True

        return False
