def get_steps_lst(in_data: str) -> list:
    res = ''

    for el in in_data:
        if el.isdigit():
            res += el

        else:
            res += f' {el} '

    res = res.split()

    for i in range(len(res)):
        if res[i].isdigit():
            res[i] = int(res[i])

    return res


def get_steps_count(lst_in: list) -> int:
    count = 0
    
    for el in lst_in:
        if type(el) == str:
            count += 1

    return count


def process_step(lst_in: list):
    lst_work = lst_in[:] # lst_in.copy()
    if ('/' in lst_work) or ('*' in lst_work):
        for i in range(len(lst_work)):
            if lst_work[i] == '/':
                temp = lst_work[i - 1] / lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break

            elif lst_work[i] == '*':
                temp = lst_work[i - 1] * lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break
    else:
        for i in range(len(lst_work)):
            if lst_work[i] == '+':
                temp = lst_work[i - 1] + lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break

            elif lst_work[i] == '-':
                temp = lst_work[i - 1] - lst_work[i + 1]
                del lst_work[i-1 : i+2]
                lst_work.insert(i - 1, temp)
                break

    return lst_work
