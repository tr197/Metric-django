from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Category, CategorySub
from product.serializeres import CategorySerializer, ProductSerializer


class ListCategory(APIView):
    
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializers = CategorySerializer(categories, many=True)
            data = { 'categories': serializers.data }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print('[erorr] [-ListCategory-API-]')
            return Response({
                    'message': '1001'
                    }, status=status.HTTP_503_SERVICE_UNAVAILABLE )
            
            
class ListProduct(APIView):
    
    def get(self, request, category_id):
        
        try:
            category = CategorySub.objects.get(id=category_id)
            products = category.products.all()
        except ObjectDoesNotExist as e:
            category = Category.objects.get(id=category_id)
            products = category.products.all()
            
            sub_categories = category.children.all()
            for sub in sub_categories:
                products = products.union(sub.products.all())        
            
        serializers = ProductSerializer(products, many=True)
        return Response({
            'products': serializers.data
            }, status=status.HTTP_200_OK)
