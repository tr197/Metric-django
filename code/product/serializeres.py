from rest_framework import serializers
from product.models import Category, CategorySub, Product, ProductOptions


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
    price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'main_image_url', 'description']
        
    def get_price(self, obj):
        return obj.calculate_price()


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptions
        fields = ['name', 'description', 'price']
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    options = ProductOptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image_urls', 'description', 'options']
        
    def get_price(self, obj):
        return obj.calculate_price()