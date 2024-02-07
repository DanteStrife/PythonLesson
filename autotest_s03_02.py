"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `list_1` и `k` для проверки
"""

list_1 = [1, 12, 6, 11, 8, 15]
k = 11

# Введите ваше решение ниже

out = 0

for i in range(0, len(list_1)):
        if k - list_1[i] == 1 or k - list_1[i] == -1:
            out = list_1[i]
for i in range(0, len(list_1)):
    if list_1[i] == k:
        out = list_1[i]

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]

out1 = min(list_1, key=lambda x: abs(x - k))


print(out)
print(number)
print(out1)

