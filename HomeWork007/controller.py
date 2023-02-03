import gui
import save_to_file


def move(select):
    if select == "1":
        save_to_file.write_to_files(gui.read_data())
    if select == "2":
        gui.print_guide()
