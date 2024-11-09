from django.urls import path
from .views import books_author_view, DisplayingLibraryDetails

urlpatterns = [
    path('', view=books_author_view , name='books-view'),
    path('library/<int:pk>/', view=DisplayingLibraryDetails.as_view() , name='library'),
]   
