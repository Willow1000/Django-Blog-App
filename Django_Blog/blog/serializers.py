from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    # blogger = serializers.CharField()
    class Meta:
        model = Blog
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"

