from rest_framework.permissions import AllowAny
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView
from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(permission_classes=(AllowAny, )), name='register'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name="user_update"),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name="user_destroy"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny, )), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny, )), name='token_refresh'),
]
