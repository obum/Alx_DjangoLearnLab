# accounts/serializers.py
from tkinter import S
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'bio', 'profile_picture']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email', ''),
#             bio=validated_data.get('bio', ''),
#             profile_picture=validated_data.get('profile_picture', ''),
#             password=validated_data['password']
#         )
#         return user


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField()
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        # Create the user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        # Generate a token for the user
        Token.objects.create(user=user)
        return user
