# Задача №25 Напишите программу которая принимает на вход строки
# и отслеживает сколько раз каждый символ уже встречался.
#  Колличество повторов добавляется к символам с помощью
# посфикса формата _n.
#
# Для решения используйте функцию .split()

# stream = [a, a, a, b, c, a, a, d, c, d, d]


stream = input('Введите символы через пробел: ').split()
my_dit = {}
for el in stream:
    if el not in my_dit:
        print(el, end=' ')
    else:
        print(f'{el}_{my_dit[el]}', end=' ')
    my_dit[el] = my_dit.get(el, 0) + 1
