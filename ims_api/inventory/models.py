from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self): 
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name= 'items')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self): 
        return self.name