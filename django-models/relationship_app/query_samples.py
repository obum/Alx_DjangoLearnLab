from relationship_app.models import Author, Book, Library, Librarian

#  “List all books in a library.” task

# Assuming library_name
library_name = "Alor library"

# Get the library object
library = Library.objects.get(name=library_name)

# Fetch the titles of books in the specified library
books_in_library = library.books.all()

# Display the book titles
for title in books_in_library:
    print(title)


#  “Query all books by a specific author.” task

author_name = 'Chinwe Achebe'

author = Author.objects.get(name=author_name)

all_book_by_author = Book.objects.filter(author=author)

for book in all_book_by_author:
    print(book)
    
# Retrieve the librarian for a library.

library_name = 'Ogun State Library'

library = Library.objects.get(name=library_name)

the_librarain = Librarian.objects.get(library=library)

print(the_librarain.name)