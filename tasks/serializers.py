from rest_framework import serializers
from .models import User, Task, Category, Priority, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'user', 'task']
        read_only_fields = ['id', 'created_at', 'user']

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    priority = PrioritySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'deadline', 
            'priority', 'status', 'user', 'category', 
            'created_at', 'updated_at', 'comments'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']