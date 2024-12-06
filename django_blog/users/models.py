from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        # do a validation
        if not email:
            raise ValueError('Email is required')
        # code to create user
        user = self.model(
            email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)
        
        return user
        
    def create_superuser(self, email, password):
        # We call the create user funtion and change the attributes
        
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        

class User(AbstractUser):
# enter additional profile / user data fields
    email = models.EmailField(unique=True, max_length=200)
    username = models.CharField(unique=False, max_length=10)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    objects = UserManager() # The object that will control the creation of users
    



    
