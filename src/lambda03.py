a = (1, 2, 3, 4)
b = (1, 2, 3, 4)

x = lambda x, y: x * y

y = list(map(x, a, b))
print(y)