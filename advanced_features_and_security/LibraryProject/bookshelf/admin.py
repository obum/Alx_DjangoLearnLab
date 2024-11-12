from django.contrib import admin
from .models import Book
from .models import Book, Author, CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', "profile_photo")
    # search_fields = ('name', 'books')
    
admin.site.register(CustomUser, CustomUserAdmin)