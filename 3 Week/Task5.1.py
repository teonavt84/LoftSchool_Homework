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


def country_dict(data_list: list) -> list:
    result = []
    for element in data_list:
        try:
            if len(element) < 5:
                raise ValueError
            dict_county = {'Country': element[1], 'Town': element[0], 'Population': max(element[2:4]),
                           'Square': element[4]}
            result.append(dict_county)
        except ValueError:
            result.append('ValueError')
    return result


for i, el in enumerate(data_country):
    print(f'{el} -> {country_dict(data_country)[i]}')
