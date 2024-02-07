"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

list_01 = [1, 1, 2, 0, -1, 3, 4, 4]

print(len(set(list_01)))

list_02 = []
for el in list_01:
    if el not in list_02:
        list_02.append(el)
print(len(list_02))

list_03 = []
for i in range(len(list_01)):
    if list_01[i] not in list_03:
        list_03.append(list_01[i])
print(len(list_03))

