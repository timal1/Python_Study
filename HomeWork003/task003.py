# Task3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
list = [1.1, 1.2, 3.1, 5, 10.01]
min = list[0] % 1
max = list[0] % 1

for i in range(len(list)):
    if max < list[i] % 1:
        maxIndex = i
    if min > list[i] % 1:
        minIndex = i

print(round(list[maxIndex] % 1 - list[minIndex] % 1, 2))
