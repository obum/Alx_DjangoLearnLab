from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet

from .models import Category, InventoryItem
from .serializers import InventoryItemSerializer, CategorySerializer

# Create your views here.

class InventoryItemView(ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        # Ensure that logged_in_users can only access their own inventory items
        queryset = InventoryItem.objects.filter(owner=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        # Automatically assigns the logged_in_user as the owner of the inventory item upon creation
        serializer.save(owner=self.request.user)
        
class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    