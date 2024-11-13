from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
# @permission_required('app_name.can_edit', raise_exception=True)

@permission_required('bookshelf.can_edit', raise_exception=True)
def home(request):
    all_books = Book.objects.all()
    books = {'books': all_books}
    return render(request, template_name='bookshelf/book_list.html', context= books)