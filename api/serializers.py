from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['id','name']

class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.SlugRelatedField(
        source='category',
        read_only=True,
        slug_field='name'
    )
    class Meta :
        model = Task
        fields = ['id','description','is_completed','category','category_name','created_at']
