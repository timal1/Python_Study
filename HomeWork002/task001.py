# Task1: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
#  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число N = "))


def listProductNumbers(n):

    list = []
    for n in range(n):
        i = 1
        productNumbers = 1
        while i <= n + 1:
            productNumbers = productNumbers * i
            i += 1
        list.append(productNumbers)

    return list


print(f"Набор произведений чисел от 1 до {n} = {listProductNumbers(n)}")
