"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""

lst_01 = [0, -1, 5, 2, 3]

count = 0
for i in range(1, len(lst_01)):
    if lst_01[i] > lst_01[i -1]:
        count += 1
print(count)


res_01 = []             # Ищем нечетные элементы
for el in lst_01:
    if lst_01[i] % 2 == 1:
        res_01.append(el)
print(res_01)


res_02 = []
for i in range(0, len(lst_01), 2):
    if lst_01[i] % 2 == 1:
        res_02.append(lst_01[i])
print(res_02)


# print(count for i in range(1, len(lst_01)) if lst_01[i] > lst_01[i - 1] count += 1)
