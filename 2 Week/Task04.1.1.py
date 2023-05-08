# 4. Функции.
# Задача 1.
# Напишите функцию, которая заменяет числа в переданном ей списке по схеме:
# все вхождения минимального числа заменить на максимальное число.
# Техническое задание:
# 1. Функция принимает один аргумент - список целых чисел.
# 2. Возвращает новый список с заменой минимального числа(всех вхождений) на максимальное число.
# 3. Если ни одна замена не была произведена, функция возвращает None.
# Примеры/Тесты:
# <function_name>([1, 3, 1, 3, 4, 2, 5, 5, 2]) -> [5, 3, 5, 3, 4, 2, 5, 5, 2]
# Т.е. все 1 заменены на 5.
# <function_name>([2, 3, 2, 3, 4, 2, 4, 4, 2]) -> [4, 3, 4, 3, 4, 4, 4, 4, 4]
# Т.е. все 2 заменены на 4.
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
data = [1, 3, 1, 3, 4, 2, 5, 5, 2]
# data = [2, 3, 2, 3, 4, 2, 4, 4, 2]
# data = [3, 3, 3, 3, 3, 3, 3, 3, 3]
func_min_max = False
func_text = ''
if func_min_max == True:
    func_text = 'min-max'
else:
    func_text = 'max-min'

def replacing_digits(num, func_min_max):
    max_num = max(num)
    min_num = min(num)
    data_new = num.copy()
    if func_min_max == False:
        max_num, min_num = min_num, max_num
    for i, el in enumerate(data_new):
        if data_new[i] == min_num:
            data_new[i] = max_num
    if num == data_new:
        return None
    return data_new


data_new = replacing_digits(data, func_min_max)

print(f'<replacing_digits>({data}, {func_text}) -> {data_new}')
