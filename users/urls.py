from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("", UserListAPIView.as_view(), name="users-list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="users-retrieve"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="users-update"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="users-delete"),
]