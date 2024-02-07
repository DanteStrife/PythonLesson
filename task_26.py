# Пример. вспомнить предыдущее

def f(*args):
    return sum(args)


print(f(5, 3, 5, 1))

print((lambda *args: sum(args))(1, 2, 3))
func = lambda *args: sum(args)
print(func(5, 6, 8, 3, 4))


def f(**kwargs):
    # return kwargs['a'] + kwargs['b'] + kwargs['c']
    return  sum(kwargs.values())

print(f(a=1, b=2, c=3))  # именнованные

