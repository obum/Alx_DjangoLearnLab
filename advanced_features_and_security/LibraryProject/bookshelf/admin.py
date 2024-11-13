from django.contrib import admin
from .models import Book
from .models import Book, CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)

admin.site.register(CustomUser, UserAdmin)