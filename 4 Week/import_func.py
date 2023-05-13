import func_min_max as utils
list_num = [1, 2, 3, 4, 5, 6]
try:
    print(f'{list_num} -> {utils.min_max(list_num)}')
except ValueError:
    print(f'{list_num} -> ValueError')

