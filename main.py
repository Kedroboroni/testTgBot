import telebot
from telebot import types

bot = telebot.TeleBot("7242578162:AAGe1G8znafwQQA_3n4awLjzOKMtX1MXKkI")

@bot.message_handler(commands = ["start", "main", "hello"])
def main(message):
    print(type(message))
    bot.send_message(message.chat.id, "вывели дефотное сообщние")



@bot.message_handler(content_types = ["photo"])
def processingPhoto(message):
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("перейти на сайт", url = "http://127.0.0.1:8000/"))
    #markup2 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Удалить сообщение", callback_data = "delete")
    btn2 = types.InlineKeyboardButton("Изменить сообщение", callback_data = "edit")
    markup.row(btn1,btn2)
    bot.send_message(message.chat.id, "Вау, ты отправил мне фотографию", reply_markup = markup)





bot.polling(none_stop = True)