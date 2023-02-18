import telebot
from telebot import types
from controllers import process_func
from loggers import logger

with open('TOKEN.txt', 'r', encoding='utf-8') as file:
    token = file.read()


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(
        message, "/start - запускает бота,  /help - посмотреть команды")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "Введите математическое выражение")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    result = process_func(message.text)

    logger(message.from_user.id, message.text, result)

    bot.reply_to(message, f'Результат вычисления: {message.text} = {result}')


bot.infinity_polling()
