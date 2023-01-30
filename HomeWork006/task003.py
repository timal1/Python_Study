# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11
from functools import reduce

number = [int(s) for s in input("Введите число ") if s.isdigit()]
sumMembersNumber = reduce(lambda x, y: x+y, number)
print(sumMembersNumber)
