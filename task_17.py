"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0 = 0, a1 = 1,
ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# n = 7
# fib_p, fib_n = 0, 1
# for _ in range(n):
#     fib_p, fib_n = fib_n, fib_p + fib_n
# print(fib_n)

def fibon(n, fibo_p=0, fibo_n=1):
    if n == 0:
        return fibo_n
    return fibon(n-1, fibo_n, fibo_p + fibo_n)
print(fibon(7))
