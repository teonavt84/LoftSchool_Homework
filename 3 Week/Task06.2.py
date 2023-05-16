# Задача 2. Изменить предыдущую задачу
# Техническое задание:
# - Теперь функция должна возвращать не список, а генератор целых четных чисел в заданном диапазоне.
# - Использовать генераторное выражение
# - Остальные условия остаются прежними
# - Вызвать функцию для некоторых аргументов.
# - Проверить тип возвращаемого объекта.
# - Исчерпать итератор в цикле for. Например, вывести все значения через запятую.
# Вызвать функцию для некоторых аргументов.
# Исчерпать итератор в цикле while с помощью функции next(), дойти до исключения StopIteration
def func_list_num(begin: int, end: int) -> list:
    if end < begin:
        raise ValueError
    if begin % 2 == 1 and end % 2 == 1 and begin == end:
        raise ValueError
    list_num = (num for num in range(begin, end + 1) if num % 2 == 0)
    return list_num


begin = int(input('Введите число 1: '))
end = int(input('Введите число 2: '))


# try:
#     list_num = func_list_num(begin, end)
#     print(list_num)
#     print(f'({begin}, {end})', end=' -> ')
#     for num in list_num:
#         print(f'{num}', end=', ')
# except ValueError:
#     print(f'({begin}, {end}) -> ValueError')

try:
    list_num = func_list_num(begin, end)
    print(list_num)
    print(f'({begin}, {end})', end=' -> ')
    while True:
        print(next(list_num))
except ValueError:
    print(f'({begin}, {end}) -> ValueError')
