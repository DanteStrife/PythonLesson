"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""

# 0 1 1 2 3 5 8 13

a = 5
fibo_p, fibo_next = 0, 1
i = 2
while fibo_next < a:
    fibo_p, fibo_next = fibo_next, fibo_p + fibo_next
    i += 1
if a == fibo_next:
    print(i)
else:
    print(-1)

"""
fibo_p = 0, fibo_next = 1
fibo_p = 1, fibo_next = 2
fibo_p = 2, fibo_next = 3
fibo_p = 3, fibo_next = 5

"""

