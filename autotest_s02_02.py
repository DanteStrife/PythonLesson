s = 12
p = 27
x = 0
y = 0

solutions = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if s == i + j and p == i * j:
            solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
    print(solution[0], solution[1])

c = 0
for x in range(s + p):
    if c:
        break
    for y in range(s + p):
        if x + y == s and s * y == p:
            c = 1
            print(*sorted([x, y]))
            break


def find_numbers(s, p):
    result = []
    for x in range(1, s + 1):
        y = s - x
        if x * y == p and x <= y:
            result.append((x, y))

    return result


pairs = find_numbers(s, p)

for pair in pairs:
    print(*pair)

for x in range(1, s + 1):
    if p % x == 0:
        y = p // x
        if x + y == s and x <= y <= 1000:
            print(x, y)

