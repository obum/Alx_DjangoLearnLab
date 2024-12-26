from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, InventoryItemSerializer
from .models import Category, InventoryItem
from rest_framework import permissions
from django.contrib.auth import get_user_model
from .permissions import IsOwnerorReadonly
# Create your views here.

User = get_user_model()

class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class InventoryItemViewset(ModelViewSet):
    serializer_class = InventoryItemSerializer
    queryset = InventoryItem.objects.all()
    # Only authenticated users should be able to manage inventory (i.e., create, update, or delete items)
    permission_classes = [permissions.IsAuthenticated, IsOwnerorReadonly]

