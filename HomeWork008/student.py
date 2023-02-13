import os


def input_data():
    studentName = input("Введите свою фамилию: ")
    subject = input(
        "Введите предмет, или ничего не вводите чтобы увидеть оценки по всем предметам: ")
    data = [studentName, subject]
    return data


def print_score(data):
    fileName = f'{data[0]}'.lower() + '.txt'

    if (os.path.exists(fileName)):
        strings = []
        with open(fileName, 'r', encoding='utf-8') as file:
            strings = file.readlines()
            count = 0
            print("\n Ваши оценки: ")
            for string in strings:
                str1 = string.split(" ")
                if (str1[0] == data[1]):
                    print(string)
                    count = 1
                if (data[1] == ""):
                    print(string)
                    count = 1

            if (count == 0):
                print(f'По {data[1]} у вас нет оценок')

    else:
        print("У вас пока нет оценок")
