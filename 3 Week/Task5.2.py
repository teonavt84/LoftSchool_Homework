import LSpt5_t1_data as data

data_country = data.data


def country_dict(data_list):
    result = []
    for element in data_list:
        try:
            if len(element) < 5:
                raise ValueError
            country_dict = {'Country': element[1], 'Town': element[0], 'Population': max(element[2:4]), 'Square': element[4]}
            result.append(country_dict)
        except ValueError:
            continue
    return result


def group_by_country(data):
    res = country_dict(data)
    result = {}
    for element in res:
        country = element['Country']
        town = element['Town']
        population = element['Population']
        square = element['Square']
        if country not in result:
            result[country] = []
        result[country].append({'town': town, 'population': population, 'square': square})
    return result


city_info = group_by_country(data_country)

for country, cities in city_info.items():
    print(country)
    for city in cities:
        print(city)
