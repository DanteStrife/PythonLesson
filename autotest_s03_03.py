"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение  `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `k` для проверки
"""

k = 'ноутбук'

# Введите ваше решение ниже

count = 0

points = {1:'AEIOULNSTRАВЕИНОРСТ', 2:'DGДКЛМПУ', 3:'BCMPБГЁЬЯ', 4:'FHVWYЙЫ', 5:'KЖЗХЦЧ', 8:'JXШЭЮ', 10:'QZФЩЪ'}

for i in k:
    for key, value in points.items():
        if i.upper() in value:
            count += key

word = k.upper()  # переводим все буквы в верхний регистр

count1 = 0

for i in word:
    for j in points:
        if i in points[j]:
            count1 = count1 + j

print(count)
print(count1)
