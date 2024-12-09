from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import HabitsConfig
from .views import HabitViewSet

appname = HabitsConfig.name

router = DefaultRouter()
router.register("habits", HabitViewSet, basename="habit")


urlpatterns = [
    path("", include(router.urls)),

]
