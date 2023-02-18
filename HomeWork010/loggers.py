from datetime import datetime


def logger(userId, inputData, result):
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(
            f'Идетификатор пользователя: {userId}; Введенное выражение: {inputData}; Результат: {result}\n')
