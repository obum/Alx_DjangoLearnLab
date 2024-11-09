from django.shortcuts import render
from .models import Library
from .models import Book

from django.views.generic.detail import DetailView

library_name = "Alor library"

# Get the library object


# Create your views here.

def list_books(request):
    
    books = Book.objects.all()
    
    context = {'books': books}
    
    return render(request, template_name='relationship_app/list_books.html', context=context)


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'
