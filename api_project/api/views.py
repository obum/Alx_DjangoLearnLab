from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookSerializers
from api.models import Book
# Create your views here.

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
