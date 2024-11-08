from django.db import models

# Create your models here.
class Book(models.Model):
    # CharField with a maximum length of 200 characters.
    title = models.CharField(max_length=200)
    # CharField with a maximum length of 100 characters.
    author = models.CharField(max_length=100)
    # IntegerField.
    publication_year = models.IntegerField()
    
    def __str__(self) -> str:
        c_names = [field.name for field in Book._meta.get_fields()]
        data = zip(c_names, (self.id, self.title, self.author, self.publication_year))
        instance_descr = ''
        for att in data:
            instance_descr += f'{att[0]}: {att[1]}\n'
        return instance_descr
        # return f"Book id: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPuplication year: {self.publication_year}"