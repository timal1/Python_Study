# Task4: Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input("Введите число N = "))


def calculateSumEvenNumbers(n):
    sum = 0

    for n in range(n + 1):
        if n % 2 == 0:
            sum = sum + n
    return sum


print(f"Сумма четных чисел от 1 до {n} = {calculateSumEvenNumbers(n)}")
