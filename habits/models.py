from django.db import models
from django.conf import settings
from rest_framework.exceptions import ValidationError

class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь"
    )
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время выполнения")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    linked_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="linked_to",
        verbose_name="Связанная привычка"
    )
    periodicity = models.PositiveIntegerField(default=1, verbose_name="Периодичность (в днях)")
    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Вознаграждение"
    )
    time_to_complete = models.PositiveIntegerField(verbose_name="Время выполнения (в секундах)")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action} ({self.user.email})"

    def clean(self):
        # Привычка может иметь только одно из двух: вознаграждение или связанную привычку
        if self.reward and self.linked_habit:
            raise ValidationError("Привычка не может одновременно иметь вознаграждение и связанную привычку.")

        # Приятная привычка не может иметь вознаграждения или связанных привычек
        if self.is_pleasant and (self.reward or self.linked_habit):
            raise ValidationError("Приятная привычка не может иметь вознаграждения или связанных привычек.")

        # Время выполнения не больше 120 секунд
        if self.time_to_complete > 120:
            raise ValidationError("Время выполнения не может превышать 120 секунд.")

        # Периодичность должна быть не меньше 1 раза в 7 дней
        if self.periodicity < 1:
            raise ValidationError("Периодичность выполнения должна быть не реже, чем раз в 7 дней.")

        # Только приятные привычки могут быть связаны
        if self.linked_habit and not self.linked_habit.is_pleasant:
            raise ValidationError("Связанной привычкой может быть только приятная привычка.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
