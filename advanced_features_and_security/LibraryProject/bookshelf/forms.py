from django import forms

# Forms are elegate means to add and edit data in our web app

from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year')
        

