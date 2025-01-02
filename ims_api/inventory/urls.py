from django.urls import path
from .views import InventoryItemView, CategoryView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', InventoryItemView, basename='inventory')
router.register('category/', CategoryView, basename='category')

urlpatterns = []

urlpatterns += router.urls