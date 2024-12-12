from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.

# class UserManager(BaseUserManager):

#     def createuser(self, ):
#         ...

#     def createsuperuser():
#         ...

class User(AbstractUser):
    email = models.EmailField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(name='profile_picture', upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    # objects = UserManager()

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

