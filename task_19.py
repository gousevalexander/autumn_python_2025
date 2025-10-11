#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
# .....

f = open('algoritm.csv', 'w', encoding='utf-8')
for i in range(10):
    f.write(f'{i + 1}) "{algoritm[i]}"\n')
f.close()