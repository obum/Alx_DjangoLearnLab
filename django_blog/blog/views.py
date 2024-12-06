from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from .models import Post, Profile
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
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
    
    
class ListPostsView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    context_object_name = 'post'
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'
    # form_class = form  
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePostView, self).form_valid(form)
    

class ProfileView(LoginRequiredMixin, DetailView): 
    """
    view used to handle the display of a user profile
    By consuming the generic.DetailView and outputing the profile_detail.html
    """
    model = Profile
    template_name = 'blog/profile_detail.html'
    context_object_name = 'profile' # name used to reference the class/object in the templates
    
    def get_object(self):
        """Return the profile of the currently logged-in user."""
        return self.request.user.profile

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     ...

@login_required
def ProfileUpdateView(request):
    
    user = request.user # Get the logged-in user
    profile = user.profile  # Assuming OneToOne relationship, get the proflie of the user
    
    if request.method == 'POST':
        # create a user_form and profile_form instance that gets & handles the data passed by the user
        user_form = UserForm(request.POST, instance=user) 
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save() # Save the changes to the user model
            profile_form.save() # Save the changes to the profile model
            return redirect('profile-view')  # Redirect to profile detail page
    else:
        # Initialize the forms with existing data, if the user request is not a POST request
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    
    return render(request, 'blog/profile_update.html', context)

class DetailPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    
class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_update.html'
    fields = [ 'title', 'content']
    
    # success_url = reverse_lazy('post-detail', args=['post.id'])
        
    def get_success_url(self):
            # Use reverse_lazy to dynamically pass the pk of the created object
            return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'   
    fields = '__all__'
    success_url = reverse_lazy('posts')
    
    def test_func(self):
        post =  self.get_object()
        return post.author == self.request.user

    def handle_no_permission(self):
    # Redirect to a custom "access denied" page
        return redirect('home')