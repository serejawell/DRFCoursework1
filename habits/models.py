from django.db import models

from config import settings

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец привычки",
        help_text="Укажите владельца привычки",
        blank=True,
        null=True
    )

    place = models.CharField(
        max_length=250,
        verbose_name="Место действия",
        help_text="Укажите место действия",
    )
    time_action = models.TimeField(
        verbose_name="Время действия", help_text="Укажите время действия"
    )
    action = models.CharField(
        max_length=250, verbose_name="Действие", help_text="Укажите действие"
    )
    is_nice = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Укажите признак приятной привычки",
        **NULLABLE,
    )

    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        **NULLABLE,
    )
    frequency = models.IntegerField(
        default=7,
        verbose_name="Периодичность",
        help_text="Укажите периодичность привычки",
    )
    remuneration = models.CharField(
        max_length=250,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
        **NULLABLE,
    )
    lead_time = models.PositiveIntegerField(
        default=120,
        verbose_name="Время на выполнение",
        help_text="Укажите время на выполнение",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="Укажите признак публичности",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"