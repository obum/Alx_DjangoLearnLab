from rest_framework import permissions

# Implement permission checks to ensure that users can only manage their own inventory items.

class IsOwnerorReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.created_by == request.user