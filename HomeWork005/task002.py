# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# 1 | 2 | X
# 4 | X | O
# X | 8 | O

def printGameBoard(list):
    print("----------")
    print(f'{list[0]} | {list[1]} | {list[2]}')
    print("----------")
    print(f'{list[3]} | {list[4]} | {list[5]}')
    print("----------")
    print(f"{list[6]} | {list[7]} | {list[8]}")


def gameIfPositionClose(list, position):
    if list[position[1]] == "X" or list[position[1]] == "O":
        print("Эта позиция уже занята")
        return False
    else:
        return True


def gamePosition(list, position):
    if gameIfPositionClose(list, position):
        list[position[1]] = position[0]
        return True
    else:
        return False


def gameWin(list, simbol):
    if list[0] == list[1] == list[2] == simbol or list[3] == list[4] == list[5] == simbol or list[6] == list[7] == list[8] == simbol or list[0] == list[3] == list[6] == simbol or list[1] == list[4] == list[7] == simbol or list[2] == list[5] == list[8] == simbol or list[0] == list[4] == list[8] == simbol or list[2] == list[4] == list[6] == simbol:
        printGameBoard(list)
        print(f"Выиграл игрок, который ставил {simbol}")
        return 1
    else:
        return 0


def game():
    faild = list('123456789')
    win = 0
    gamer = "X"

    while win == 0:
        printGameBoard(faild)
        position = (gamer, int(
            input(f"Введите номер позиции на которую поставить {gamer} ")) - 1)
        if gamePosition(faild, position):
            win = gameWin(faild, gamer)
            if gamer == "X":
                gamer = "O"


game()
