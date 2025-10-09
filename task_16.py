# todo: База данных пользователя.
# Задан массив объектов пользователя

# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

def choose_sort_type():
    print('''Выберите тип сортировки:
              1. По возрасту
              2. По первой букве
              3. По группе''')
    return int(input('Тип сортировки: '))

def choose_value():
    return input('Введите критерии поиска: ')

def print_result(res):
    print('Результат: ')
    ages_1 = [1, 21, 31, 41, 51, 61, 71, 81]
    ages_2 = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 73, 73, 74]
    for d in res:
        if d['age'] in ages_1:
            years = 'год'
        elif d['age'] in ages_2:
            years = 'года'
        else:
            years = 'лет'
        print(f"Пользователь: '{d['login']}' возраст {d['age']} {years}, группа '{d['group']}'")

input_ = choose_sort_type()
match input_:
    case 1:    # отсев по возрасту
        age = int(choose_value())
        res = list(filter(lambda d: d['age'] >= age, users))
        print_result(res)
    case 2:   # отсев по первой букве имени
        letter = choose_value()
        res = list(filter(lambda d: d['login'][0] == letter.upper(), users))
        print_result(res)
    case 3:   # отсев по группе
        group = choose_value()
        res = list(filter(lambda d: d['group'] == group.lower(), users))
        print_result(res)
