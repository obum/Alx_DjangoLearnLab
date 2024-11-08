from relationship_app.models import Book, Library, Librarian

# Checks for “List all books in a library.” task

# Assuming library_id = 1
library_name = 'Alor library'

# Get the library object
library = Library.objects.get(name='Alor library')

# Fetch the titles of books in the specified library
books_in_library = Book.objects.all().filter(ibraries_found=library)

# Display the book titles
for title in books_in_library:
    print(title)
