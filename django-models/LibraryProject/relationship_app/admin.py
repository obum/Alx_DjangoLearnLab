from django.contrib import admin
from .models import Book, Author, Librarian, Library, UserProfile

# Register your models here.

admin.site.register(Book)

admin.site.register(Author)

admin.site.register(Librarian)

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_book_count', 'display_books')
    search_fields = ('name', 'books')
admin.site.register(Library, LibraryAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    # search_fields = ('name', 'books')
admin.site.register(UserProfile, UserAdmin)
