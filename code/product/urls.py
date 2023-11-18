from django.urls import path
from product import api

urlpatterns = [
    path('categories', api.ListCategory.as_view()),
]
