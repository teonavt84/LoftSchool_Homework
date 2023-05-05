# Усложнение #1 для задания #3 [*]
# Решите для числа произвольной разрядности: произвольное количество цифр в числе.
# Учтите, что цифр в числе теперь может быть нечетное количество. Проверяйте это и выдавайте значимое диагностическое
# сообщение пользователю.
num = input('Введите номер билета: ')
# len_num = int(len(num) // 2)
len_num = len(num) // 2
left_side = num[0:len_num]
right_side = num[len_num:]
if len_num % 2 == 1:
    left_side = num[0:len(num) // 2]
    right_side = num[(len(num) // 2)+1:]
sum_left_side = 0
sum_right_side = 0
i = 0
while i < len_num:
    sum_left_side = sum_left_side + int(left_side[i])
    sum_right_side = sum_right_side + int(right_side[i])
    i += 1
if sum_left_side == sum_right_side:
    print('Yes')
else:
    print('No')
