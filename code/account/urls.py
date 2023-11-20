from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'account'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]