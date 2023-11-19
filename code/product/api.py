from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Category, CategorySub, Product
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
                    }, status=status.HTTP_404_NOT_FOUND )
            
            
class ListProduct(APIView):
    
    def get(self, request, category_id):
        try:
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
        except Exception as e:
            print(e)
            return Response({'message': '1002'}, status=status.HTTP_404_NOT_FOUND)



class ProductView(APIView):
    
    def get(self, request, product_id):
        
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product, many=False)
            return Response({
                'product': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': '1003'}, status=status.HTTP_404_NOT_FOUND)