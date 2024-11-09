from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import UserProfile

def librarian_view(request):
    # Check if the user is authenticated and has the 'Librarian' role
    if not request.user.is_authenticated or request.user.userprofile.role != 'Librarian':
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'relationship_app/librarian_page.html')  # Replace with your actual template