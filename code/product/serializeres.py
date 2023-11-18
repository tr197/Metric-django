from rest_framework import serializers
from product.models import Category, CategorySub


class CategorySubSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySub
        fields = ['id', 'name']
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    
    children = CategorySubSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'children']