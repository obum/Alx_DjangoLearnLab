from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    # author is a Foreign key from the author model and can be accessed from the author model as books
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title
    
# Library Model:
# name: CharField.
# books: ManyToManyField to Book.

class Library(models.Model):
    name = models.CharField(max_length=50)
    # books has a ManytoMany rel. to the Library model and can be accessed from the book model as libraries_found
    books = models.ManyToManyField(Book, related_name='Libraries_found')

    def display_books(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(book.title for book in self.books.all()[:3])

    display_books.short_description = 'Books'

    def display_book_count(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return len(self.books.all())

    display_book_count.short_description = 'Count of Books'

# Librarian Model:
# name: CharField.
# library: OneToOneField to Library.

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    # library has a OnetoOne rel. to the Librarian model and can be accessed from the Library model as libraries_found
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='Librarian')
