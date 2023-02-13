import os


def input_data():
    studentName = input("Введите фамилию ученика: ")
    subject = input("Введите предмет: ")
    score = input("Введите введите оценку: ")
    data = [studentName, subject, score]
    return data


def save_to_file(data):
    fileName = f'{data[0]}'.lower() + '.txt'

    if (os.path.exists(fileName)):
        strings = []
        with open(fileName, 'r', encoding='utf-8') as file:
            strings = file.readlines()
            final = [""]
            count = 0
            for string in strings:
                str1 = string.split(" ")
                if (str1[0] == data[1]):
                    string = string.replace("\n", "")
                    string = string + " " + data[2] + "\n"
                    count = 1
                final.append(string)
            if (count == 0):
                final.append(data[1] + " " + data[2])
        with open(fileName, 'w', encoding='utf-8') as files:
            files.writelines(final)
    else:
        with open(fileName, 'w', encoding='utf-8') as file1:
            file1.write(f'{data[1]} {data[2]}')
