from rest_framework import serializers
from product.models import (
    Category, CategorySub,
    Product, ProductOptions,
    ProductComments,
) 
from shop.serializeres import PlatformSerializer


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
    
    platform = PlatformSerializer(many=False)
    class Meta:
        model = ProductOptions
        fields = ['name', 'platform', 'price', 'sale_count', 'link']
        

class ProductCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductComments
        fields = ['username', 'content', 'create_date']

  

        
class ProductDetailSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    options = ProductOptionSerializer(many=True, read_only=True)
    comments = ProductCommentSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image_urls', 'description', 'options', 'comments']
        
    def get_price(self, obj):
        return obj.calculate_price()