from django.db import models 
# from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default="")
    
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, null=True, blank=True, default='my bio')
    profile_pic = models.ImageField(null=True, blank=True, default='profile picture', upload_to='profile_pics/')
    
    def __str__(self):
        return f'{self.user.username} Profile'