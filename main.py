import telebot
from telebot import types

bot = telebot.TeleBot("7242578162:AAGe1G8znafwQQA_3n4awLjzOKMtX1MXKkI")


@bot.message_handler(commands = ["start"])
def keyBoard(message):
    markup = types.ReplyKeyboardMarkup() #Создали меняю разметки
    btn1 = types.KeyboardButton("перейти на сайт") #Создали кнопку
    btn2 = types.KeyboardButton("Удалить сообщение") #Создали кнопку
    btn3 = types.KeyboardButton("Изменить сообщение") #Создали кнопку
    markup.add(btn1) #Разместили
    markup.row(btn2, btn3) #Разместили
    bot.send_message(message.chat.id, "Привет!", reply_markup = markup)


@bot.message_handler(commands = ["start", "main", "hello"])
def main(message):
    print(type(message))
    bot.send_message(message.chat.id, "вывели дефолтное сообщние")



@bot.message_handler(content_types = ["photo"])
def processingPhoto(message):
    markup = types.InlineKeyboardMarkup() #Создали разметку
    btn1 = types.InlineKeyboardButton("перейти на сайт", url = "http://127.0.0.1:8000/") #Создали кнопку
    btn2 = types.InlineKeyboardButton("Удалить сообщение", callback_data = "delete") #Создали кнопку
    btn3 = types.InlineKeyboardButton("Изменить сообщение", callback_data = "edit") #Создали кнопку
    markup.add(btn1) #Разместили
    markup.row(btn2, btn3) #Разместили
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