# urls.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # Маршрут для получения access токена
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Маршрут для обновления refresh токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
