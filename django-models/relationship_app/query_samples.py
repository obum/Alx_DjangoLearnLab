from relationship_app.models import Book, Library, Librarian

# Checks for “List all books in a library.” task

# Assuming library_name
library_name = "Alor library"

# Get the library object
library = Library.objects.get(name=library_name)

# Fetch the titles of books in the specified library
books_in_library = library.books.all()

# Display the book titles
for title in books_in_library:
    print(title)
