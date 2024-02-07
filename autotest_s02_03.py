n = 1000
f = 1
s = 0
while f < n:
    f = 2 ** s
    s += 1
    if f <= n:
        print(f)

