from django.urls import path
from .views import books_author_view
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', view=list_books , name='books-view'),
    path('library/<int:pk>/', view=LibraryDetailView.as_view() , name='library'),
]   
