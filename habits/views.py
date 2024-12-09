from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Habit
from .serializers import HabitSerializer


class HabitPagination(PageNumberPagination):
    page_size = 5  # Пагинация по 5 привычек на странице

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только для авторизованных пользователей
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # Публичные привычки доступны всем, свои привычки — только владельцу
        if self.action == "list":
            return Habit.objects.filter(user=self.request.user)
        return Habit.objects.all()

    def perform_create(self, serializer):
        # Привязываем привычку к текущему пользователю
        serializer.save(user=self.request.user)
