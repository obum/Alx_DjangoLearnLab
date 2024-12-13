from .views import CommentViewSet, PostViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path


 # automatically creates routes for all actions 
 # (lists, create, retrieve, update, destroy)
router = DefaultRouter()

router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
