from django.urls import path
from product import api

urlpatterns = [
    path('categories/', api.ListCategory.as_view()),
    path('list-product/<str:category_id>/', api.ListProduct.as_view()),
    path('detail/<str:product_id>/', api.ProductView.as_view()),
]
