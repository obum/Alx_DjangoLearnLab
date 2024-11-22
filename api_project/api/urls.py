from django.db import router
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Route for the BookList view
    path('', include(router.urls))
]

# Mechanisim for users to obtain their tokens

from rest_framework.authtoken import views
urlpatterns += [
    path('token/', views.obtain_auth_token)
]