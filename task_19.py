"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

def func_1(n):
    for div in range(3, n):
        if n % div == 0:
            return False
        return True
print(func_1(5))

def func_2(n, div=3):
    if div < n:
        if div % n == 0:
            return False
        return func_2(n, div + 1)
    return True
print(func_2(12))
