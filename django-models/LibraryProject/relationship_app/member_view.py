from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import UserProfile

def member_view(request):
    # Check if the user is authenticated and has the 'Member' role
    if not request.user.is_authenticated or request.user.userprofile.role != 'Member':
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'relationship_app/member_page.html') 