from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Library
from .models import Book

from django.views.generic.detail import DetailView

# ----This import are used for user registration ---- #
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import login

from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})




# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'
    
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterView, self).form_valid(form)    
    

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
