# Task4: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5

# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

#     a, b, c, d, e, h - рандом

from random import randint

k = d = int(input("Введите натуральную степень k = "))

koefs = []
for i in range(k + 1):
    koefs.append(randint(0, 100))

ur = ""

i = 0
while k >= 0:
    if k == 0:
        ur = ur + f'{koefs[i]}'
    elif k == 1:
        ur = ur + f'{koefs[i]}*x + '
    else:
        ur = ur + f'{koefs[i]}*x^{k} + '
    k -= 1
    i += 1
print(f"Mногочлен степени {d} = " + ur)
