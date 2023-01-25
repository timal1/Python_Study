# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф


# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

# candies = [i for i in range(1, 121)]

from random import randint

numberOfCandies = 120
gamer = randint(0, 1)  # жребий кто первый ходит
max = 28

while (numberOfCandies != 0):
    if gamer == 0:
        numberOfCandies -= int(
            input(f"вы можете взять не более {max} конфет, сколько возьмете? = "))
        gamer = 1
        print(f' Осталось {numberOfCandies} конфет')
    else:
        a = randint(1, max + 1)
        if a > numberOfCandies or numberOfCandies <= max:
            a = numberOfCandies
        if max < numberOfCandies <= max*2:
            a = numberOfCandies - max - 1
        if max*2 < numberOfCandies <= max*3:
            a = numberOfCandies - max*2 - 1
        if max*3 < numberOfCandies <= max*4:
            a = numberOfCandies - max*3 - 1
        if max*4 < numberOfCandies <= 120:
            a = numberOfCandies - max*4 - 1
        if a == 0:
            a = 2
        numberOfCandies -= a
        print(f"Бот забрал {a} конфет")
        gamer = 0
        print(f' Осталось {numberOfCandies} конфет')

if gamer == 1:
    print("Вы победили")
else:
    print("Бот победил")
