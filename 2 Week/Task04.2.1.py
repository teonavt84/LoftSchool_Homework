# Задача 2.
# Заданы три списка строк: имена, действия и цели
# Реализовать функцию, возвращающую список строк, каждая из которых состоит
# из случайно выбранных элементов, по одному из каждого списка.
# Функция принимает аргументы: количество строк в результирующем списке и три списка со строками.
# Примеры/Тесты:
# <function_name>(2, names_all, actions_all, targets_all)
#        -> ['Катерина бежит на тренировку ', 'Федор спешит гулять ']
# <function_name>(3, names_all, actions_all, targets_all)
#       -> ['Анастасия спешит на дачу ', 'Федор спешит гулять ', 'Илья идет на тренировку ']
import random
from random import sample
names_all = ['Иван', 'Федор', 'Катерина', 'Марина', 'Илья', 'Ольга', 'Анастасия', ]
actions_all = ['гулять', 'в школу', 'на дачу', 'в магазин', 'на спортплощадку', 'на тренировку', ]
targets_all = ['идет', 'едет', 'спешит', 'бежит', 'не торопится', ]
rows = 3


def random_rows(rows, names_all, actions_all, targets_all):
    i = 0
    data = []
    res = []
    while i < rows:
        data.append(sample(names_all, 1) + sample(actions_all, 1) + sample(targets_all, 1))
        i += 1
    for el in data:
        res.append(' '.join(el))
    return res

r_rows = random_rows(rows, names_all, actions_all, targets_all)
print(r_rows)
print(dir(random))
# Не додумал