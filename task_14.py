#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

import random

def calculate_dist(mass: list):
    nums = list(set(mass))
    for i in nums:
        indexes = [(mass.index(i), 0)]
        cnt = 0
        for j in range(indexes[0][0] + 1, len(mass)):
            if mass[j] == i:
                indexes.append((j, j - indexes[cnt][0]))
                cnt += 1
        if len(indexes) > 1:
            mn = min([i[1] for i in indexes[1:]])
            new_indexes = []
            for j in range(len(indexes)):
                if indexes[j][1] == mn:
                    if indexes[j - 1][0] not in new_indexes:
                        new_indexes.append(indexes[j - 1][0])
                    new_indexes.append(indexes[j][0])
            print(f'Для числа {i} минимальное расстояние в массиве по индексам:', *new_indexes)
        else:
            print(f'Для числа {i} нет минимального расстояния, т.к. элемент в массиве один.')

mass = [random.randint(1,10) for i in range(30)]
print(mass)
calculate_dist(mass)