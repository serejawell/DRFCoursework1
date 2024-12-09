from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Используем конфигурацию из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи в каждом зарегистрированном приложении
app.autodiscover_tasks()
