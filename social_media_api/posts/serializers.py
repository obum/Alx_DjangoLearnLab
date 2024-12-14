from rest_framework import serializers
from .models import Comment, Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def validate_title(self, value):
        if Post.objects.filter(title=value).exists():
            raise serializers.ValidationError('Post with this title already exists')
        return value

class CommentSerializer(serializers.ModelSerializer):
    # Ensure that only post the exists can be commented on or referenced.
    posts = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'


