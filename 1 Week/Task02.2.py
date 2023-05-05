# Усложнение #2 для задания #2 []**
# Для числа произвольной разрядности добавить в вывод строку с числами, например так:
# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)
num = input('Введите число: ')
i = 0
sum = 0
while i < len(num):
    sum = sum + int(num[i])
    b = num[i]
    i += 1
print('Сумма чисел числа' + ' ' + str(num) + ' ' + 'равна' + ' ' + str(sum), end=' ')
print('(', end='')
i = 0
while i < len(num):
    if i == len(num)-1:
        print(str(num[i]), end='')
    else:
        print(str(num[i]), end=' + ')
    i += 1
print(')')

