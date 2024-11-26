from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    def validate_publication_year(self, value):
        """
        Ensure the publication_year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
        
class AuthorSerializer(serializers.ModelSerializer):
    
    book = BookSerializer(many=True, read_only=True) 
    # Ensure that an author's book can be accessed from the author serializer
    # "Many = False" because of the one-to-one relationship between the author and book class 
    
    class Meta:
        model = Author
        fields = ['name', 'book']
        