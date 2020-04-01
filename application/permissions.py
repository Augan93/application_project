from rest_framework.permissions import BasePermission


class ApplicationOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Доступ у создатея приложения"""
        return obj.owner == request.user
