# Task:
# Создать информационную систему позволяющую работать с учителями / учениками школы
# Учитель: Добавляет оценку, опред. ученику за опред. предмет
# Ученик: Просматривает оценки по фамилии
# Расписать функции на несколько файлов, как в предыдущем ДЗ

# Наименование предметов не стал определять, так как считаю что по умолчанию и учителя и ученики должны знать названия своих предметов в школе ;)

import controller


def run():
    controller.move(controller.choosing_an_action())


if __name__ == '__main__':
    run()
