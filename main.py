# main.py
import telebot
from config import TOKEN
import structura
import logging

from storage import record_user_messages

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bot = telebot.TeleBot(TOKEN)

structura.register_handlers(bot) # Регистрируем обработчики

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    record_user_messages(message)

print("Бот запущен")
bot.infinity_polling()