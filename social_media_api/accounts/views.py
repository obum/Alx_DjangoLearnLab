# from django.shortcuts import render #Do not need tis import
from django.db import IntegrityError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer

from rest_framework.views import APIView
from rest_framework.authentication import authenticate
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


# class RegisterView(CreateAPIView):
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         # Validate and save the user using the serializer
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception = True)
#         user = serializer.save()

#         # Ensure user is valid and token is created
#         if user is None:
#             return Response({"error": "User could not be created"}, status=HTTP_400_BAD_REQUEST)
        
#         # Generate or retrieve the token for the user
#         token, created = Token.objects.get_or_create(user=user)

#         # Prepare the response data
#         response_data = {
#             "token": token.key,
#             "user": UserSerializer(user).data
#         }
        
#         # Return the response
#         return Response(response_data, status=HTTP_201_CREATED)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     try:
    #         # Use the serializer to validate and save the data
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         user = serializer.save()  # The logic for creating the user and token is in the serializer

    #         # Return a custom response
    #         return Response({
    #             "user_info": UserSerializer(user).data,
    #             "token": user.auth_token.key  # The token is created and attached to the user in the serializer
    #         }, status=HTTP_201_CREATED)
        
    #     except IntegrityError as e:
    #         # Handle unique constraint violation (e.g., username already exists)
    #         if "UNIQUE constraint failed" in str(e):
    #             return Response({
    #                 "error": "A user with this username already exists."
    #             }, status=HTTP_400_BAD_REQUEST)
            
    #         # Catch other IntegrityErrors if needed
    #         return Response({
    #             "error": "A database error occurred."
    #         }, status=HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        token = Token.objects.get(user=user)
        if user and token:
            # # Delete any existing tokens for the user
            # Token.objects.filter(user=user).delete()
            # # Generate a new token
            # token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=HTTP_400_BAD_REQUEST)
   


class ProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Restrict to the logged-in user's profile
        return self.queryset.filter(id=self.request.user.id)

    # def update(self, request, *args, **kwargs):
    #     # Allow the user to update their profile
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)
    
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the user's token and delete it
            request.user.auth_token.delete()
            return Response({"message": "Successfully logged out."}, status=HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token not found."}, status=HTTP_400_BAD_REQUEST)