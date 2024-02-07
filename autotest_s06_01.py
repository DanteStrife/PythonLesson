# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
#
# Пример
#
# На входе:
#
#
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# На выходе:
#
#
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19

# При отправке кода на Выполнение раскомментируйте строку ниже,
# чтобы задать значения аргументов и вызвать функцию
#
# При отправке решения на Проверку закомментируйте
# эту строку обратно - система автоматически подставит
# разные значения аргументов и вызовет функцию для проверки
#
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
#
# Введите ваше решение ниже

for i in range(0, len(list_1)):
    if list_1[i] >= min_number and list_1[i] <= max_number:
        print(i)


def find_indices_in_range(lst, min_number, max_number):
    indices = [i for i, value in enumerate(lst) if min_number <= value <= max_number]
    return indices

result_indices = find_indices_in_range(list_1, min_number, max_number)
for index in result_indices:
    print(index)

