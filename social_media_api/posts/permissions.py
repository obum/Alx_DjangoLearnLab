from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only authors to modify posts.
    Anyone can view posts. Only authenticated users can create new posts.
    """

    def has_object_permission(self, request, view, obj):
<<<<<<< HEAD
    
        if request.method in permissions.SAFE_METHODS:
            # SAFE METHODS are GET HEAD OPTIONS
=======
        # Allow safe methods (GET, HEAD, OPTIONS) for any user
        if request.method in permissions.SAFE_METHODS:
>>>>>>> cffd149232b8cb57784de5db41bf372a21222130
            return True
        # Allow modification only if the user is the author
        return obj.author == request.user