# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

listNumbersAndStrings = [12, 'sadf', 5643, 'ljncsdn', 43533]

listNumbers = list(filter(lambda x: type(x) == str, listNumbersAndStrings))

listStrings = list(filter(lambda x: type(x) == int, listNumbersAndStrings))

print(listNumbers)

print(listStrings)
