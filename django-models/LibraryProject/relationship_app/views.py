from django.shortcuts import render
from .models import Book, Library

from django.views.generic import ListView, DetailView

library_name = "Alor library"

# Get the library object


# Create your views here.

def books_author_view(request):
    
    books = Book.objects.all()
    
    context = {'books': books}
    
    return render(request, template_name='relationship_app/list_books.html', context=context)


class DisplayingLibraryDetails(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'
