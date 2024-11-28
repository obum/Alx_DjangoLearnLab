from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters

from django_filters import rest_framework

from rest_framework import generics

# Create your views here.

# A ListView for retrieving all books.
class BookList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Use queryset to tell the view what database table / oject we require
    queryset = Book.objects.all()
    
    # Use serializer_class to tell the view how to format and validate the queryset data
    serializer_class = BookSerializer
    
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['title', 'publication_year', 'author']
    
    # filter_backends = [filters.SearchFilter]
    
    search_fields = ['title', 'author']
    
    ordering_fields = ['title', 'publication_year']
    
# A DetailView for retrieving a single book by ID.
class BookDetail(RetrieveAPIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Use queryset to tell the view what database table / oject we require
    queryset = Book.objects.all()
    
    # Use serializer_class to tell the view how to format and validate the queryset data
    serializer_class = BookSerializer
    
# A CreateView for adding a new book.
class BookCreate(CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    
    # Use queryset to tell the view what database table / oject we require
    queryset = Book.objects.all()
    
    # Use serializer_class to tell the view how to format and validate the queryset data
    serializer_class = BookSerializer
    
    
    
    def create(self, request, *args, **kwargs):
        # check that the title of the book is not greater than 5 characters
        if len(request.data.get('title', '')) < 5:
            return Response({'error: The title must be greater than 5 characters'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
    # Use the perform_create method to create the validated data
    def perform_create(self, serializer):
        serializer.save()
        
    
    
    
# An UpdateView for modifying an existing book.    
class BookUpdate(UpdateAPIView):
    
    permission_classes = [IsAuthenticated]
    
    # Use queryset to tell the view what database table / oject we require
    queryset = Book.objects.all()
    
    # Use serializer_class to tell the view how to format and validate the queryset data
    serializer_class = BookSerializer
    
    def update(self, request, *args, **kwargs):
        
        # get the partial status, that is if its a PUT / PATCH
        
        partial = kwargs.pop('partial', False)
        
        # get the data instance to be updated from the view instance
        # using the primarykey being passed from the url
        instance = self.get_object()
        
        if int(request.data['publication_year']) > 2024:
            return Response({'error: The publication year in the future'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Deserialize the data from the front end form
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)        
        
        return Response(serializer.data)
        # return super().update(request, *args, **kwargs)
        
    def perform_update(self, serializer):
        serializer.save()
    
# A DeleteView for removing a book. 
class BookDelete(DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    
    # Use queryset to tell the view what database table / oject we require
    queryset = Book.objects.all()
    
    # Use serializer_class to tell the view how to format and validate the queryset data
    serializer_class = BookSerializer