from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']


# Custom Creation Form
class CustomPostCreationForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']

    # Automatically set the author to the current user when saving the form
    def save(self, commit=True):
        
        post = super().save(commit=False)
        
        if not post.author:
            post.author = self.request.user # Assign the logged-in user as the author
        if commit:
            post.save()
        return post