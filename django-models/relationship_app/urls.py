from django.urls import path
from .views import list_books, LibraryDetailView, register

from .views import register

from . import views

from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register , name='register'),
    path('login/', view=LoginView.as_view(template_name='relationship_app/login.html') , name='login'),
    path('logout/', view=LogoutView.as_view(template_name='relationship_app/logout.html') , name='logout'),


    path('', view=list_books , name='books-view'),
    path('library/<int:pk>/', view=LibraryDetailView.as_view() , name='library'),

]   
