"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `list_1` и `k` для проверки
"""

list_1 = [1, 2, 3, 4, 5]
k = 3

# Введите ваше решение ниже
count = 0
for i in range(0, len(list_1)):
    if list_1[i] == k:
        count += 1

print(count)
