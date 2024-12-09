import telebot
from config.settings import TELEGRAM_API_TOKEN

API_TOKEN = TELEGRAM_API_TOKEN


def send_message_to_telegram(chat_id, message):

    bot = telebot.TeleBot(API_TOKEN)
    bot.send_message(chat_id, message)