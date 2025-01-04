# from django.shortcuts import render
# from rest_framework import generics, permissions
# from rest_framework.viewsets import ModelViewSet
# from .models import Category, InventoryItem
# from .serializers import InventoryItemSerializer, CategorySerializer

# Create your views here.

# class InventoryItemView(ModelViewSet):
#     serializer_class = InventoryItemSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def get_queryset(self):
#         # Ensure that logged_in_users can only access their own inventory items
#         queryset = InventoryItem.objects.filter(owner=self.request.user)
#         return queryset
    
#     def perform_create(self, serializer):
#         # Automatically assigns the logged_in_user as the owner of the inventory item upon creation
#         serializer.save(owner=self.request.user)
        
# class CategoryView(ModelViewSet):
#     serializer_class = CategorySerializer
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Category.objects.all()
    
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, InventoryItemSerializer
from .models import Category, InventoryItem
from rest_framework import permissions, generics, status
from rest_framework.response import Response
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

class InventoryLevelView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = InventoryItemSerializer
    queryset = InventoryItem.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = InventoryItemSerializer(queryset, many=True)
        items = serializer.data
  
        inventory_level = [
            {
                "id": item['id'],
                "name": item["name"],
                "quantity": item["quantity"]
            }
            for item in items
        ]
        
        print(inventory_level)
        return Response(
                inventory_level,
                status=status.HTTP_200_OK
            )

