from .views import CommentViewSet, PostViewSet, FeedView
from rest_framework.routers import DefaultRouter
from django.urls import include, path


 # automatically creates routes for all actions 
 # (lists, create, retrieve, update, destroy)
router = DefaultRouter()

router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feeds')
]
