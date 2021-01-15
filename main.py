import telebot
from Classes import Chat
bot = Chat("Mhyssanga")

b = telebot.TeleBot('867754051:AAGKOuI_k4xOAw7DfLNl5HBHVlSJ3fNv75U')

@b.message_handler(func=lambda message: True)
def echo_all(message):
    f = bot.escutar(message.text)
    resp = bot.pensar(f)
    bot.falar(resp)
    b.reply_to(message,resp)
    

b.polling()