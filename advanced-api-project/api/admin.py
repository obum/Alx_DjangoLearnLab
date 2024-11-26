from django.contrib import admin
from api.models import Book, Author

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_year', 'author']
    
admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'book']
    
admin.site.register(Author, AuthorAdmin)