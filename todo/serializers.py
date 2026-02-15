from rest_framework import serializers
from . models import Task, Category




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'owner', 'category', 'title', 'description', 'status', 'priority', 'created_at', 'due_date', 'updated_at']
        read_only_fields = ['owner', 'created_at', 'updated_at']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'created_at','updated_at','owner']
        read_only_fields = ['created_at','updated_at','owner']