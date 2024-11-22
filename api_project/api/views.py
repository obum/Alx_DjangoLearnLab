from django.shortcuts import render
import rest_framework
# from rest_framework.generics import ListAPIView
from .serializers import BookSerializers
from api.models import Book
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookList(rest_framework.generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
    
# Using Viewsets to simplify view creation of CRUD operation


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializers
    queryset = Book.objects.all()
    
    
#  -- A view where useres can get obtain their token
    
