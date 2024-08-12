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
    bot.send_message(message.chat.id, "Вывели дефолтное сообщние") # Обрабоатли команды старт маин хеллоу, вывели сооющение



@bot.message_handler(content_types = ["photo"])
def processingPhoto(message):
    markup = types.InlineKeyboardMarkup() #Создали разметку
    btn1 = types.InlineKeyboardButton("перейти на сайт", url = "http://127.0.0.1:8000/") #Создали кнопку с сылкой
    btn2 = types.InlineKeyboardButton("Удалить сообщение", callback_data = "delete") #Создали кнопку которая возвращает делет
    btn3 = types.InlineKeyboardButton("Изменить сообщение", callback_data = "edit") #Создали кнопку которая возвращает делет
    markup.add(btn1) #Разместили одну кнопку в строке
    markup.row(btn2, btn3) #Разместили две кнопки в строке
    bot.send_message(message.chat.id, "Вау, ты отправил мне фотографию", reply_markup = markup) #Отправили сообщение


@bot.callback_query_handler(func = lambda callback: True) #Слот для обработки нажати кнопок
def callback_message(callback):
    if callback.data == "delete": 
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1) # Удалили предидущее сообщение
    elif callback.data == "edit":
        bot.edit_message_text("Мы изменили свое сообщение, и ты нам за это нчиего не сделаешь!!!", callback.message.chat.id, callback.message.message_id ) # Удалили последнее сообщение


@bot.message_handler()
def anouther(message):
    bot.send_message(message.chat.id, "Воу-воу-воу, полегче, я еще не на столько умен, чтобы обрабоать твое сообщение!")


bot.polling(none_stop = True)