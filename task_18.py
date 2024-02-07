"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

lst = [1, 3, 3, 3, 4]
max_n = max(lst)
min_n = min(lst)
lst_after = []
for el in lst:
    if el == max_n:
        lst_after.append(min_n)
    else:
        lst_after.append(el)
print(lst_after)

def zen(lst, lst_after=[], max_n=max(lst), min_n=min(lst)):
    if len(lst) == 0:
        return lst_after
    if lst[0] == max_n:
        lst_after.append(min_n)
    else:
        lst_after.append(lst[0])
    return zen(lst[1:])
print(zen(lst))

