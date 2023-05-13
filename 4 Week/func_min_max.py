list_num = [1, 2, 1, 2, 2, 1]


def min_max(num: list) -> tuple:
    if min(num) == max(num):
        raise ValueError
    return (min(num), max(num))


if __name__ == '__main__':
    try:
        print(f'{list_num} -> {min_max(list_num)}')
    except ValueError:
        print(f'{list_num} -> ValueError')
