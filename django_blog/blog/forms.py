from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post, Profile
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


# Custom post Creation Form
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
    
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        }
    # Comment Validation
    def clean_content(self):
        
        content = self.cleaned_data.get('content', '')
        
        word_count = len(content.split())
        
        if word_count < 5:
            raise forms.ValidationError("Your comment must contain at least 5 words.")
        if word_count > 100:
            raise forms.ValidationError("Your comment cannot exceed 100 words.")
        return content
    
    # def __init__(self, *args, **kwargs):
    #     # Get the 'request' from kwargs, if available
    #     self.request = kwargs.pop('request', None)
    #     super().__init__(*args, **kwargs)

    # def save(self, commit=True): # function definition of a custom form save 
        
    #     comment = super().save(commit=False) # creates a model form instance without saving to the database
        
    #     if not comment.author: #   if the author field in the comment model is blank\
    #         if self.request:
    #             print(f"Assigning author: {self.request.user}")
    #             comment.author = self.request.user # assigns the logged-in user as the comment author
    #         else:
    #             print("No request object available")
    #     if commit: # Commit variable is defaulted to true
    #         comment.save() # save the comment to the database
    #     return comment 
        

    