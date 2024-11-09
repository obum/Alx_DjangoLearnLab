from django.shortcuts import render
from .models import Library
from .models import Book

from django.views.generic.detail import DetailView

# ----This import are used for user registration ---- #
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView



class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class CustomLoginView(LoginView):
    template_name= 'relationship_app/login.html'
    fields = '__all__'
    # redirect_authenticated_user = True
    
    
    def get_success_url(self):
        return reverse_lazy('books-view')


# Create your views here.

def list_books(request):
    
    books = Book.objects.all()
    
    context = {'books': books}
    
    return render(request, template_name='relationship_app/list_books.html', context=context)


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'
