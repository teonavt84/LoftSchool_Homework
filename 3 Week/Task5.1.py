# Задача
# Написать функцию преобразующую список в словарь.
# Техническое задание:
# Функция:
# - принимает аргумент - список вида [Город, Страна, Население в 2018 году, Население сейчас, Площадь]
# - возвращает словарь вида {"country":xxxx, "town": xxxx, "population":xxxx, "square":xxxx}
# Где население(population) - максимальное из двух населений города.
# Если данные извлечь невозможно - отсутствует площадь (такое будет в данных) -
# функция поднимает исключение ValueError
# Проверить работоспособность функции на приведенных данных из файла LSpt5_t1_data.py.
# Для этого импортировать файл LSpt5_t1_data.py под псевдонимом в свой код.
# При определении функции использовать Аннотации и проверки типов(type hinting)
# Примеры/Тесты:
# <function_name>(["Мумбаи", "Индия", 19980000, 23645000, 881,]) -> {"country":"Индия", "town": "Мумбаи","population":23645000, "square":881}
# <function_name>(["Циндао", "Китай", 5381000,]) -> ValueError
import LSpt5_t1_data as data
data_country = data.data


def county_list(data):
    for element in data:
        try:
            dict_county = {'Country': element[0], 'Town': element[1], 'Population': max(element[2:4]),
                           'Square': element[4]}
            print(f'{element} -> {dict_county}')
        except IndexError:
            print('Невозможно извлечь данные.')


county_list(data_country)
