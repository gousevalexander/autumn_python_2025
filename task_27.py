#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

letters = ' abcdefghijklmnopqrstuvwxyz'
nums = [letters[int(i)] if i.isdigit() and int(i) < 27 else i for i in input('Введите числа через пробел: ').split()]
print(''.join(nums))
