# Задача 1.
# Пользователь вводит номер года с клавиатуры. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите  сообщение вида "Год xxxx является високосным",
# иначе "Год xxxx не является високосным".
# В соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100; или если он
# кратен 400.
year = input("Введите год: ")
if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    year_true = True
else:
    year_true = False
print("Год " + year + " является високосным") if year_true else print("Год " + year + " не является високосным")