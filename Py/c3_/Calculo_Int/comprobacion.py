from fractions import Fraction

def generar_sucesion(formula, n):
    sucesion = []
    for i in range(n):
        valor = eval(formula.replace('n', str(i+1)))
        sucesion.append(valor)
    return sucesion

def generar_sucesion_fraccion(formula, n):
    sucesion = []
    for i in range(n):
        valor = eval(formula.replace('n', str(i+1)))
        sucesion.append(Fraction(valor).limit_denominator())
    return sucesion

var = input(str('''La formula es normal o fraccion:
1.- N
2.- F
'''))

if var == 'N':

    formula_decimal = input('Introduce la formula: ')
    cantidad_elementos_decimal = 10

    sucesion_generada_decimal = generar_sucesion(formula_decimal, cantidad_elementos_decimal)
    print(sucesion_generada_decimal)

elif var == 'F':

    formula_fraccion = input('Introduce la formula: ')
    cantidad_elementos_fraccion = 10

    sucesion_generada_fraccion = generar_sucesion_fraccion(formula_fraccion, cantidad_elementos_fraccion)
    print(sucesion_generada_fraccion)