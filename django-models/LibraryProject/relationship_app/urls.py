from django.urls import path
from .views import list_books, LibraryDetailView, CustomLoginView

from .views import RegisterView

from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', view=RegisterView.as_view() , name='register'),
    path('login/', view=CustomLoginView.as_view() , name='login'),
    path('logout/', view=LogoutView.as_view() , name='logout'),


    path('', view=list_books , name='books-view'),
    path('library/<int:pk>/', view=LibraryDetailView.as_view() , name='library'),

]   
