from django.urls import path
from .views import home, book_new

urlpatterns = [
    path('', home, name='book-list'),
    path('add/book/', book_new , name='book-new')
]
