"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

Ввод:
7
3 1 3 4 2 4 12

6
4 15 43 1 15 1

Вывод:
3 3 2 12
"""

lst_1 = [3, 1, 3, 4, 2, 4, 12]

lst_2 = [4, 15, 43, 1, 15, 1]

lst_3 = []

for el in lst_1:
    if el not in lst_2:
        lst_3.append(el)
print(lst_3)

lst_3 = [el for el in lst_1 if el not in lst_2]
print(lst_3)

set_1 = {1, 2, 3}
set_2 = set()
for el in set_1:
    set_2.add(el ** 2)
print(set_2)

set_2 = {el ** 2 for el in set_1}
print(set_2)

dict_1 = {1: 'one', 2: 'two', 3: 'three'}
dict_2 = {}
for el, s in dict_1.items():
    dict_2[el] = s
print(dict_2)

dict_2 = {el: s for el, s in dict_1.items()}
print({el: s for el, s in dict_1.items()})

my_lst = list(map(int, input("Введите числа через пробел: ").split()))
print(my_lst)
