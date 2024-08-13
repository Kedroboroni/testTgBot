import telebot
from telebot import types

bot = telebot.TeleBot("7242578162:AAGe1G8znafwQQA_3n4awLjzOKMtX1MXKkI")
API = "41bc5d5f636a36078cb732f482d9ce0a"

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, напиши свой город")


@bot.message_handler(content_types = ["text"])
def get_country(message):
    country = message.text.strip().lower()


bot.polling(none_stop = True)
