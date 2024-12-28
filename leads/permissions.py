# leads/permissions.py
from rest_framework import permissions

class IsKAMOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               (request.user.is_staff or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.assigned_to == request.user