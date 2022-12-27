# Task3: Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]


n = int(input("Введите число N = "))
listIndexes = [2, 2, 3, 1, 5]
listNumbers = [i for i in range(-n, n + 1)]


def productNumbersByIndex(n):
    i = 1
    productNumbers = listNumbers[listIndexes[0]]

    while i < len(listIndexes):
        productNumbers = productNumbers * listNumbers[listIndexes[i]]
        i += 1

    return productNumbers


print(
    f" Произведение элементов массива {listNumbers} \n на индексах: {listIndexes} = {productNumbersByIndex(n)}")
