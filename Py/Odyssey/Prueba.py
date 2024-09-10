def f(x, y):
    return x**2 - 1/y**2

# Método de Euler
def euler_method(x0, y0, h, target_x):
    x = x0
    y = y0
    
    while x < target_x:
        y += h * f(x, y)
        x += h
        
    return y

# Condiciones iniciales y tamaño de paso
x0 = 0
y0 = 2
h = 0.3
target_x = 2

# Aplicar el método de Euler
approx_y = euler_method(x0, y0, h, target_x)

print("Valor aproximado de y(2) usando el método de Euler:", approx_y)sxdss
