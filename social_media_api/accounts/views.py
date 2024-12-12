# from django.shortcuts import render #Do not need tis import
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer

from rest_framework.views import APIView
from rest_framework.authentication import authenticate
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_serializer().instance
        token, created = Token.objects.get_or_create(user=user)
        response.data = {"token": token.key, "user": UserSerializer(user).data}
        return response

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            # Delete any existing tokens for the user
            Token.objects.filter(user=user).delete()
            # Generate a new token
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=HTTP_400_BAD_REQUEST)
   


class ProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Restrict to the logged-in user's profile
        return self.queryset.filter(id=self.request.user.id)

    def update(self, request, *args, **kwargs):
        # Allow the user to update their profile
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

