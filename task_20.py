#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

f = open('inverted_sort.txt', 'at+', encoding='utf-8')
f.seek(0)
text_list = f.readlines()
text_list = text_list[::-1]
print(*text_list, sep='')
f.writelines(text_list)
f.close()
