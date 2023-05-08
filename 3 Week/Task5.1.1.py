import LSpt5_t1_data as data

data_country = data.data


def country_dict(town: str, country: str, population_2018: int, population_now: int, square: int) -> list:
    result = []
    dict_country = {'Country': country, 'Town': town, 'Population': max(population_2018, population_now),
                    'Square': square}
    result.append(dict_country)
    return result


for element in data_country:
    try:
        if len(element) < 5:
            raise ValueError
        print(f'{element} -> {country_dict(*element)}')
    except ValueError:
        print(f'{element} -> ValueError')