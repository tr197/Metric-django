from rest_framework import serializers
from product.models import Category, CategorySub, Product, ProductImages


class CategorySubSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySub
        fields = ['id', 'name']
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    
    children = CategorySubSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'children']
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'main_image_url', 'other_image_urls', 'description']
        