from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, HomeView, ListPostsView, ProfileView, ProfileUpdateView, CreatePostView

from .views import DetailPostView, EditPostView, DeletePostView 

from .views import CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit', ProfileUpdateView, name='profile-edit'),
    path('', HomeView.as_view(), name='home'),
    path('posts/', ListPostsView.as_view(), name='posts'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),    
    path('post/<int:pk>/', DetailPostView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', EditPostView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
    # path('posts/', ListCommentsView.as_view(), name='comments'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),    
    path('post/<int:pk>/comment/<int:comment_id>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('post/<int:pk>/comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  
    # path('comment/<int:pk>/', DetailCommentView.as_view(), name='comment-detail'),

]
