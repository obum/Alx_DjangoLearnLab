from rest_framework.response import Response # For customized responses
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
from .permissions import IsAuthorOrReadOnly

# Implement permision for only author to modify posts


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'content'] # Exact match filtering
    search_fields = ['title', 'content'] # search partial match
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        # Automatically set the author as the current user
        serializer.save(author=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author as the current user
        serializer.save(author=self.request.user)