# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

with open("1.txt", "r") as infile:
    value = infile.readline()


def zipStr(value):
    result = ""
    count = 0
    sim = value[0]
    i = 0
    while i < len(value):

        if sim == value[i]:
            count += 1
        else:
            result = result + f"{count}" + sim
            count = 1
            sim = value[i]

        if i == len(value) - 1:
            result = result + f"{count}" + sim

        i += 1
    return result


def unZipStr(string):
    i = 0
    result = ""
    while i < len(string) - 1:
        result = result + string[i + 1] * int(string[i])
        i += 2
    return result


print(value)
print(zipStr(value))
print(unZipStr(zipStr(value)))
