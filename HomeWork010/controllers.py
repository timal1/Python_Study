from models import (
    get_steps_lst,
    get_steps_count,
    process_step
)


def process_func(values: str):
    lst_steps = get_steps_lst(values)

    count_steps = get_steps_count(lst_steps)

    res_lst = lst_steps[:]

    for _ in range(count_steps):
        res_lst = process_step(res_lst)

    return res_lst[0]


def user_input() -> str:
    pass
