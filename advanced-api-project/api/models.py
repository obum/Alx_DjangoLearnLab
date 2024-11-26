from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=30)
    publication_year = models.IntegerField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='book')
    
    def __str__(self):
        return self.title