import telebot
from telebot import types

bot = telebot.TeleBot("7242578162:AAGe1G8znafwQQA_3n4awLjzOKMtX1MXKkI")

@bot.message_handler(commands = ["start", "main", "hello"])
def main(message):
    print(type(message))
    bot.send_message(message.chat.id, "вывели дефолтное сообщние")



@bot.message_handler(content_types = ["photo"])
def processingPhoto(message):
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("перейти на сайт", url = "http://127.0.0.1:8000/"))
    btn1 = types.InlineKeyboardButton("Удалить сообщение", callback_data = "delete")
    btn2 = types.InlineKeyboardButton("Изменить сообщение", callback_data = "edit")
    markup.row(btn1,btn2)
    bot.send_message(message.chat.id, "Вау, ты отправил мне фотографию", reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "edit":
        bot.edit_message_text("Мы изменили свое сообщение, и ты нам за это нчиего не сделаешь!!!", callback.message.chat.id, callback.message.message_id )


@bot.message_handler()
def anouther(message):
    bot.send_message(message.chat.id, "Воу-воу-воу, полегче, я еще не на столько умен, чтобы обрабоать твое сообщение!")

bot.polling(none_stop = True)