from random import randint
import telebot

with open('TOKEN.txt', 'r', encoding='utf-8') as file:
    token = file.read()


bot = telebot.TeleBot(token)

max = 28
numberOfCandies = "120"

with open('bot.txt', 'w', encoding='utf-8') as file1:
    file1.write(numberOfCandies)


@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.reply_to(
        message, f" На столе лежит 120 конфет, берете конфеты по очереди с Ботом, можно взять не более {max} конфет. Победитель - тот, кто оставил на столе 0 конфет. Введите количество конфет, которое хотите взять?")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(
        message, "/start - запускает бота,  /help - посмотреть команды")


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    with open('bot.txt', 'r', encoding='utf-8') as file:
        x = int(file.read())

    x = x - int(message.text)

    if (x == 0):
        messageOut = "Осталось {x} конфет, Вы победили"
    else:
        messageOut = f' Осталось {x} конфет,'
        a = randint(1, max + 1)
        if a > x or x <= max:
            a = x
        if max < x <= max*2:
            a = x - max - 1
        if max*2 < x <= max*3:
            a = x - max*2 - 1
        if max*3 < x <= max*4:
            a = x - max*3 - 1
        if max*4 < x <= 120:
            a = x - max*4 - 1
        if a == 0:
            a = 2
        x -= a

    if (x == 0):
        messageOut = f"Бот забрал {a} конфет и ПОБЕДИЛ"
    else:
        messageOut = messageOut + \
            f' Бот забрал {a} конфет, теперь осталось {x} конфет, сколько конфет возьмёте?'

    with open('bot.txt', 'w', encoding='utf-8') as file1:
        file1.write(f'{x}')

    bot.reply_to(message, messageOut)


bot.infinity_polling()
