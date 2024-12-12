from django.urls import path, include
from .views import LoginView, RegisterView, ProfileViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views  

router = DefaultRouter()

# Router to handle Get profile and obtain profile requests
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
]

# A mechanism for clients to obtain a token given the username and password.
# REST framework provides a built-in view to provide this behavior. 
urlpatterns += [
    path('token', views.obtain_auth_token)
]
