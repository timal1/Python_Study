# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв
# Ответ:
# привет ограбпв

import telebot

with open('TOKEN.txt', 'r', encoding='utf-8') as file:
    token = file.read()


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "Введите любой текст и я удалю слова содержащие 'абв'")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(
        message, "/start - запускает бота,  /help - посмотреть команды")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, " ".join(list(filter(lambda str: "абв" not in str,
                                               [i for i in message.text.split()]))))


bot.infinity_polling()
