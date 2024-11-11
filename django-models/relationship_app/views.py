from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Library
from .models import Book

from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import permission_required

# ----This import are used for user registration ---- #
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import login

from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import user_passes_test


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

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Add a book logic
    return render(request,template_name='relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request):
    # Edit a book logic
    return render(request,template_name='relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    # Delete a book logic
    return render(request,template_name='relationship_app/delete_book.html')

def list_books(request):
    
    books = Book.objects.all()
    
    context = {'books': books}
    
    return render(request, template_name='relationship_app/list_books.html', context=context)


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'


def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')