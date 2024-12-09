from celery import shared_task

from config.settings import TELEGRAM_TOKEN
from .models import Habit
import requests

def send_telegram_message(chat_id, message):
    bot_token = TELEGRAM_TOKEN
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message,
    }
    response = requests.post(url, data=data)
    return response.json()

@shared_task
def send_habit_reminder_telegram(habit_id):
    habit = Habit.objects.get(id=habit_id)
    user = habit.user
    if user.telegram_chat_id:
        message = f"Привет, {user.first_name or 'друг'}! Напоминаем тебе выполнить привычку: {habit.action} в {habit.time}."
        send_telegram_message(user.telegram_chat_id, message)
