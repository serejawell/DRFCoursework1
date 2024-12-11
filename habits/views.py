from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


# Create your views here.
class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated)
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(owner=user)
        return queryset


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,IsOwner)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = HabitPagination