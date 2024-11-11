from django.urls import path
from .views import list_books, LibraryDetailView, CustomLoginView

# from .views import RegisterView
from . import views
from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView

from .admin_view import admin_view
from .member_view import member_view
from .librarian_view import librarian_view



urlpatterns = [
    # path('register/', view=RegisterView.as_view() , name='register'),
    path('register/', views.register , name='register'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html') , name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html') , name='logout'),


    path('', view=list_books , name='books-view'),
    path('library/<int:pk>/', view=LibraryDetailView.as_view() , name='library'),
    
    path('admin-page/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),

]   
