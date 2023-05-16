# Задача 1. Сформировать список целых четных чисел в заданном диапазоне
# Техническое задание:
# Написать функцию
# - аргументы - границы диапазона. Два целых числа.
# - возвращаемое значение - список чисел.
# Для формирования списка использовать Comprehensions.
# Последовательность чисел должна быть неубывающая, если это сделать невозможно функция поднимает исключение ValueError.
# Примеры/Тесты:
# <function_name>(1,10) -> [2, 4, 6, 8, 10]
# <function_name>(1,13) -> [2, 4, 6, 8, 10, 12]
# <function_name>(-2,14) -> [-2, 0, 2, 4, 6, 8, 10, 12, 14]
# <function_name>(1,-10) -> ValueError

def func_list_num(begin: int, end: int) -> list:
    list_num = []
    if end < begin:
        raise ValueError
    if begin == end:
        raise ValueError
    list_num = [num for num in range(begin, end+1) if num % 2 == 0]
    return list_num


begin = int(input('Введите число 1: '))
end = int(input('Введите число 2: '))
try:
    list_num = func_list_num(begin, end)
    print(f'({begin}, {end}) -> {list_num}')
except ValueError:
    print(f'({begin}, {end}) -> ValueError')