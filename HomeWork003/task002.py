# Task2: Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 9, 3, 5, 7, 8]
sum = 0

for i in range(int(len(list) / 2)):
    product = list[i] * list[len(list) - 1 - i]
    print(product, end=" ")
