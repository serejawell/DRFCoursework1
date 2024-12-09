from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Укажите телефон",
        **NULLABLE
    )
    tg_nick = models.CharField(
        max_length=50,
        verbose_name="Телеграм ник",
        help_text="Укажите ник телеграма",
        **NULLABLE
    )
    tg_id = models.CharField(
        max_length=50,
        verbose_name="Телеграм id",
        help_text="Укажите телеграм id",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Укажите аватар",
        **NULLABLE
    )
    city = models.CharField(
        max_length=35, verbose_name="Страна", help_text="Укажите город", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"