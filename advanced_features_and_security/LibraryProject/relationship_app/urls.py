from django.urls import path
from .views import list_books, LibraryDetailView, CustomLoginView

# from .views import RegisterView
from . import views
from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView


from .views import admin_view, librarian_view, member_view



urlpatterns = [
    # path('register/', view=RegisterView.as_view() , name='register'),
    path('register/', views.register , name='register'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html') , name='login'),
    # path('login/', CustomLoginView.as_view() , name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html') , name='logout'),


    path('', view=list_books , name='books-view'),
    path('library/<int:pk>/', view=LibraryDetailView.as_view() , name='library'),
    
    path('admin-page/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
    
    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book'),

]   
