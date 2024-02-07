n = 123456

s = n // 1000
f1 = s % 10
s = s // 10
f2 = s % 10
s = s // 10

a = f1 + f2 + s

r1 = n % 10
r = n // 10
r2 = r % 10
r = (r // 10) % 10

b = r1 + r2 + r
if a == b:
    print("yes")
else:
    print("no")
