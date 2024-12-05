from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class CreateBookTest(APITestCase):
    # APITestCase gives us accesss to a client for accessing requests
    
    def test_should_not_create_book(self):
        # Arrange - Data need for test
        a_book = {
            'title': 'The Bible',
            'publication_year': '1234',
            'author': 'Holy Spirit'
        }
        # Act - send a request
        response = self.client.post(reverse('book-create'), a_book)
        
        # Assert
        self.assertEqual(response.status_code,  status.HTTP_403_FORBIDDEN)
        
    # response.data
    def test_create_user(self):
        
        User.objects.create_superuser(username='testuser', password='12345')

        self.client = APIClient()
        response = self.client.login(username='testuser', password='12345')
        
        self.assertEqual(response,  True)
        
        
      
        
        
        