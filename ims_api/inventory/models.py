from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

class InventoryItem(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=15, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='items')
    created_at = models.DateTimeField(default=now,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=40, null=True, blank=True)
    
    
class InventoryChange(models.Model):
    
    class ChangeSign(models.IntegerChoices):
        RESTOCK = 1, 'restock'
        SOLD = -1, 'sold'
        NO_CHANGE = 0, 'no change'
       
        
    change_reason =  models.IntegerField(
        choices=ChangeSign.choices,
        default=ChangeSign.NO_CHANGE,
    )    
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='inventory_changes')
    change_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory_changes')
    
    def save(self, *args, **kwargs):
        # Calculate the net change in inventory if it is not a no change action
        if self.change_reason != self.ChangeSign.NO_CHANGE:
            net_change = self.change_reason * self.change_quantity
            item = self.inventory_item
            
            # check for negative inventory
            if net_change < 0 and ((item.quantity + net_change) < 0):
                raise ValueError("insufficient stock for this operation")
            
            # Else Update the inventory item's quantity
            item.quantity += net_change
            item.save()
        return super().save(*args, **kwargs)
    
    
