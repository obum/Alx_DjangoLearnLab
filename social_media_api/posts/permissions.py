from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Args: self, request, view, obj
        permissions (IsAuthorOrReadOnly): Allow only authors to modify posts while unauthenticated users can view
    """
    def has_object_permission(self, request, view, obj):
        print()
        if request.method == permissions.SAFE_METHODS:
            # SAFE METHODS are GET HEAD OPTIONS
            return True
        # SAFE METHODS are PUT / PATCH / POST / DELETE
        return obj.author == request.user
