from .forms import CustomUserCreationForm
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from .models import Post
# Create your views here.


# Define the registeration view
class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = CustomUserCreationForm  # This must be a custom form class
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        
        user = form.save() # Save the user to the database
        
        messages.success(self.request, "Account created successfully! You can now log in.")

        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
class HomeView(ListView):
    model = Post
    context_object_name = 'home'
    template_name = 'blog/base.html'
    
    
class PostView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/base.html'
    

class ProfileView(ListView):
    ...