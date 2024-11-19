from django.shortcuts import render
import rest_framework
# from rest_framework.generics import ListAPIView
from .serializers import BookSerializers
from api.models import Book
# Create your views here.

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
