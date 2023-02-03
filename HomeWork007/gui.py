def read_data():
    lastName = input("Введите Фамилию: ")
    firstName = input("Введите Имя: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите дополнительную информацию: ")
    data = [lastName, firstName, phone, description]
    return data


def choosing_an_action():
    return input("Введите <1>, чтобы добавить запись или <2> чтобы распечатать справочник: ")


def print_guide():
    with open("guide1.txt", "r", encoding="utf-8") as f:
        print(*f)
