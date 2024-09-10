def swap(x, y):
    temp = x[0]
    x[0] = y[0]
    y[0] = temp

a = [1]
b = [2]

print('Antes del intercambio: a = {}, b = {}'.format(a[0], b[0]))
swap(a, b)
print('Despues del intercambio a = {}, b = {}'.format(a[0], b[0]))