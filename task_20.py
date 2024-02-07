"""
Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""
my_str = '3 4'
def func_1(n):
    my_res = ''
    for el in reversed(my_str):
        my_res += el
    return my_res
print(func_1(my_str))

def func_2(f):
    if len(f) == 1:
        return f
    return f[-1] + func_2(f[:-1])
print(func_2(my_str))
