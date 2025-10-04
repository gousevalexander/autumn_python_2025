# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.

starting_year = 1984
year = int(input('Введите номер года: '))
animal_number = abs(year - starting_year) % 12
color_number = abs(year - starting_year) % 60

match animal_number:
    case 0:
        animal = 'крысы'
    case 1:
        animal = 'коровы'
    case 2:
        animal = 'тигра'
    case 3:
        animal = 'зайца'
    case 4:
        animal = 'дракона'
    case 5:
        animal = 'змеи'
    case 6:
        animal = 'лошади'
    case 7:
        animal = 'овцы'
    case 8:
        animal = 'обезьяны'
    case 9:
        animal = 'курицы'
    case 10:
        animal = 'собаки'
    case 11:
        animal = 'свиньи'

match color_number:
    case num if 0 <= num <= 11:
        color = ('зелёного', 'зелёной')
    case num if 12 <= num <= 23:
        color = ('красного', 'красной')
    case num if 24 <= num <= 35:
        color = ('жёлтого', 'жёлтой')
    case num if 36 <= num <= 47:
        color = ('белого', 'белой')
    case num if 48 <= num <= 59:
        color = ('чёрного', 'чёрной')

print(f'Год {color[animal_number in [0, 1, 5, 6, 7, 8, 9, 10, 11]]} {animal}')
