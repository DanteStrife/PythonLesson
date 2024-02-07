coins = [0, 1, 0, 1, 1, 1, 0, 0, 0]

count1 = 0
count2 = 0

for elem in coins:
    if elem == 1:
        count1 += 1
    else:
        count2 += 1
if count1 < count2:
    print(count1)
else:
    print(count2)

