# Task1:  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input("Введите цифрой день недели от 1 до 7 = "))
if a == 6 or a == 7:
    print('Этот день является выходным')

else:
    print('Этот день не является выходным')
