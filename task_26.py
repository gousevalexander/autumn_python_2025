#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

def count_letters(poem):
    f = open(poem, encoding='utf-8')
    text = f.read()
    total_letters = len(text)
    d = {}
    letters = ['а', 'о', 'е', 'и', 'у', 'ы', 'э', 'ю', 'я']
    for letter in letters:
        d[letter] = (text.count(letter) + text.count(letter.upper())) / total_letters
    f.close()
    return d

def compare(t1, t2, t3):
    for k in t1[0].keys():
        mx = (max([t1, t2, t3], key=lambda x: x[0][k]))
        print(f'Поэт, у которого чаще других встречается буква "{k}" - {mx[1]}. Частота появления - {round(mx[0][k] * 100, 2)}%')


esenin = (count_letters('esenin.txt'), 'Есенин')
lermontov = (count_letters('lermontov.txt'), 'Лермонтов')
pushkin = (count_letters('pushkin.txt'), 'Пушкин')

compare(esenin, lermontov, pushkin)
