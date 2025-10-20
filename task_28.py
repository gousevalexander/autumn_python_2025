#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

letters = 'abcdefghijklmnopqrstuvwxyz'
text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
for i in range(1, 27):
    new_line = []
    for c in text:
        if c in letters:
            ind = letters.index(c)
            new_line.append(letters[ind - i])
        else:
            new_line.append(c)
    print(''.join(new_line), 'сдвиг =', i)
