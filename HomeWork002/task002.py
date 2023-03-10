# Task2: Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int(input("Введите число N = "))


def min_divider(n, d=2):
    return d if n % d == 0 else min_divider(n, d + 1)


print(f"Наименьший натуральный делитель целого числа {n} = {min_divider(n)}")
