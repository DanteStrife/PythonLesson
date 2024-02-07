lst = [10, 11, 13, 14]
for elem in lst:
    if elem % 2 == 0:
        print(f'{elem} - Четное')
    else:

        print(f'{elem} - Нечетное')

for i in range(1, len(lst)):
    if lst[i] % 2 == 0:
        print(f'{lst[i]} - Четное')
    else:
        print(f'{lst[i]} - Нечетное')

count = 0
while count < len(lst):
    if lst[count] % 2 == 0:
        print(f'{lst[count]} - Четное')
    else:
        print(f'{lst[count]} - Нечетное')
    count += 1

