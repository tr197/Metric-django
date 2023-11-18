from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Category, CategorySub
from product.serializeres import CategorySerializer


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