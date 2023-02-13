import teacher
import student


def move(select):
    if select == "1":
        teacher.save_to_file(teacher.input_data())
    if select == "2":
        student.print_score(student.input_data())


def choosing_an_action():
    return input("Введите <1>, если вы учитель или <2> если вы ученик: ")
