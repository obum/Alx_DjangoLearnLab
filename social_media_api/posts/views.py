from operator import pos
from rest_framework.response import Response # For customized responses
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
# from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
# from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from django_filters import rest_framework
from .permissions import IsAuthorOrReadOnly
from rest_framework.generics import ListAPIView

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'content'] # Exact match filtering
    search_fields = ['title', 'content'] # search partial match
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        # Automatically set the author as the current user
        print(f"Authenticated User: {self.request.user}")
        print(f"Authenticated User: {self.request.user}, Is Authenticated: {self.request.user.is_authenticated}")
        serializer.save(author=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author as the current user
        serializer.save(author=self.request.user)
        
class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Post.objects.all()
    
    def get_queryset(self):
        
        # Get the current user
        
        logged_in_user = self.request.user
        print(logged_in_user)
        
        # Get the users the logged in user is following
        following_users = logged_in_user.following.all()
        print(following_users)
        # Fetch posts from those users, ordered by creation date (most recent first)
        posts_by_following = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
        print(posts_by_following)
        return posts_by_following