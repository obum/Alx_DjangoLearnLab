from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, InventoryItemViewset, InventoryLevelView

router = DefaultRouter()
router.register(r'category', CategoryView, basename='category')
router.register(r'', InventoryItemViewset, basename='inventory')

urlpatterns = [
    path('level/', InventoryLevelView.as_view(), name='inventory-level'),

    path('', include(router.urls)),
]