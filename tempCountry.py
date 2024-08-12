import telebot
from telebot import types

bot = telebot.TeleBot("7242578162:AAGe1G8znafwQQA_3n4awLjzOKMtX1MXKkI")


@bot.message_handler(comands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, напиши свой город")


@bot.message_handler(content_types = ["text"])
def get_country(message):
    country = message.text.strip().lower()


bot.infinity_polling(none_stop = True)
