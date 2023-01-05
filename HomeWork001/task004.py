# Task4: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1, y1 = int(input("Введите значение x1 = ")), int(
    input("Введите значение y1 = "))
x2, y2 = int(input("Введите значение x2 = ")), int(
    input("Введите значение y2 = "))

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)

print(f"Расстояние между точками A1(x1, y1) и A2(x2, y2) r = {round(d, 2)}")