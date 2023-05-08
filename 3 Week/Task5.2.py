# Задача 2.
# Написать функцию, которая будет собирать информацию по городам.
# Техническое задание:
# Функция:
# – принимает аргумент - список списков (городов) (см.LSpt5_t1_data.py)
# – возвращает словарь вида: Ключ - Страна, Значение - список словарей
# – Для извлечения данных о конкретном городе используйте функцию, созданную в задании 1: скопируйте ее код в код программы.
# – Корректно обрабатывайте исключения ValueError, которое она будет поднимать, в этом случае в итоговый словарь город не включается.
# – При определении функции использовать Аннотации и проверки типов(type hinting).
# – Список из LSpt5_t1_data.py скопируйте себе в код программы.
# Пример:
# {"Страна", [
#           {"town1": xxxx, "population": xxxx, "square": xxxx}
#           {"town1": xxxx, "population": xxxx, "square": xxxx}
#           {"town1": xxxx, "population": xxxx, "square": xxxx}
#           ]
# }
# <function_name>(data) -> словарь
#
# Проверьте: Для Японии
# [{'town': 'Токио', 'population': 38505000, 'square': 8223},
# {'town': 'Осака', 'population': 19281000, 'square': 3004},
# {'town': 'Нагоя', 'population': 10240000, 'square': 3704},
# {'town': 'Фукуока', 'population': 5551000, 'square': 505}]
#
# Для России [{'town': 'Москва', 'population': 16555000, 'square': 5698}]
import LSpt5_t1_data as data

data_country = data.data


def group_by_country(data: list) -> dict:
    result = {}
    for element in data:
        try:
            if len(element) < 5:
                raise ValueError
            country = element[1]
            town = element[0]
            population_2018 = element[2]
            population_now = element[3]
            square = element[4]
            if country not in result:
                result[country] = []
            result[country].append({'town': town, 'population': max(population_2018, population_now), 'square': square})
        except ValueError:
            continue
    return result


result = group_by_country(data_country)
for country, cities in result.items():
    print(country)
    for city in cities:
        print(city)
    print()
