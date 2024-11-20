from django.shortcuts import render
import rest_framework
# from rest_framework.generics import ListAPIView
from .serializers import BookSerializers
from api.models import Book
from rest_framework import viewsets
# Create your views here.

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
    
# Using Viewsets to simplify view creation of CRUD operation

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
    
