from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name


urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habits-list"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits-retrieve"),
    path("create/", HabitCreateAPIView.as_view(), name="habits-create"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits-update"),
    path(
        "<int:pk>/delete/",
        HabitDestroyAPIView.as_view(),
        name="habits-delete",
    ),
    path("public/", PublicHabitListAPIView.as_view(), name="public-habits-list"),
]