from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import UserProfile

def admin_view(request):
    # Check if the user is authenticated and has the 'Admin' role
    if not request.user.is_authenticated or request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'relationship_app/admin_page.html') 