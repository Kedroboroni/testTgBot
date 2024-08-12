import telebot
from telebot import types

bot = telebot.TeleBot("7404560580:AAHAbYNTfQ95DFbu2wQM0EFvw2PDRN0GUi4")


@bot.message_handler(comands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, напиши свой город")


@bot.message_handler(content_types = ["text"])
def get_country(message):
    country = message.text.strip().lower()


bot.polling(none_stop = True)
