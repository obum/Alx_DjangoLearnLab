from django.db import models 
# from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
User = get_user_model()
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default="")
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
  
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    
    def __str__(self):
        return f"{self.author.username}'s Comment on {self.post}"
    
class Tag(models.Model):
    # name = models.ManyToManyField(Post, though='TagPost', blank=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    
    def __str__(self):
        return self.name
    
class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.tag}-{self.post}'
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, null=True, blank=True, default='my bio')
    profile_pic = models.ImageField(null=True, blank=True, default='profile picture', upload_to='profile_pics/')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    

    
    
