resultados = {
    
}
def suma (v1,v2):
    total_suma = int(v1)+int(v2)
    return total_suma
def resta (v1,v2):
    total_resta = int(v1)-int(v2)
    return total_resta
def divicion (v1,v2):
    total_divicion = int(v1)/int(v2)
    return total_divicion
def multiplicacion (v1,v2):
    total_multiplicacion = int(v1)*int(v2)
    return total_multiplicacion
def potencia (v1,v2):
    total_potencia = int(v1)**int(v2)
    return total_potencia
def sum_fracc (num1, den1):
    resden = int(den1)*int(den2)
    res1 = int(num1)*int(den2)
    res2 = int(den1)*int(num2)
    ulres = int(res1)+int(res2)
    print('===',ulres,'/',resden)
    return sum_fracc
def res_fracc (num1, den1):
    resden = int(den1)*int(den2)
    res1 = int(num1)*int(den2)
    res2 = int(den1)*int(num2)
    ulres = int(res1)-int(res2)
    print('===',ulres,'/',resden)
def mult_fracc (num1, den1):
    ulres = int(num1)*int(num2)
    resden = int(den1)*int(den2)
    print('===',ulres,'/',resden)
def divi_fracc (num1, den1):
    ulres = int(num1)*int(den2)
    resden = int(den1)*int(num2)
    print('===',ulres,'/',resden)

print('')
print('CALCULADORA OSIO')
print('')
print('''n = Normal
f = Fracciones
''')
tipo = input('=== ')
print('')
if tipo == 'n':
    print('============================================================================================')
    print('')
    print('Calculadora OSIO normal')
    print('')
    v1 = int(input('=== '))
    resultados.update({'resultado':v1})
    sol = 'si'
    while sol == 'si':
        v1 = int(resultados['resultado'])
        print('')
        vguar = input('opc ')
        print('')
        if vguar == '+':
            v2 = int(input('=== '))
            print('')
        elif vguar == '-':
            v2 = int(input('=== '))
            print('')
        elif vguar == '*':
            v2 = int(input('=== '))
            print('')
        elif vguar == '/':
            v2 = int(input('=== '))
            print('')
        elif vguar == '^':
            v2 = int(input('=== '))
            print('')
            
        total_suma = suma (v1,v2)
        total_resta = resta (v1,v2)
        total_divicion = divicion(v1, v2)
        total_multiplicacion = multiplicacion(v1, v2)
        total_potencia = potencia(v1, v2)
        
        if vguar == '+':
            print('===',total_suma)
            res = total_suma
        elif vguar == '-':
            print('===',total_resta)
            res = total_resta
        elif vguar == '*':
            print('===',total_multiplicacion)
            res = total_multiplicacion
        elif vguar == '/':
            print('===',total_divicion)
            res = total_divicion
        elif vguar == '^':
            print('===',total_potencia)
            res = total_potencia
            
        resultados.update({'resultado':res})

elif tipo == 'f':
    print('============================================================================================')
    print('')
    print('Calculadora OSIO de fracciones')
    sol = 's'
    while sol == 's':
        print('')
        print('============================================================================================')
        print('')
        num1 = input('=== ')
        print('')
        print(num1,'/')
        print('')
        den1 = input('=== ')
        print('')
        print(num1,'/',den1)
        print('')
        vguar = input('opc ')
        print('')
        if vguar == '+':
            num2 = int(input('=== '))
            print('')
            print(num2,'/')
            print('')
            den2 = int(input('=== '))
            print('')
            print(num2,'/',den2)
            print('')
            sum_fracc(num1, den1)
            print('')
        elif vguar == '-':
            num2 = int(input('=== '))
            print('')
            print(num2,'/')
            print('')
            den2 = int(input('=== '))
            print('')
            print(num2,'/',den2)
            print('')
            res_fracc(num1, den1)
            print('')
        elif vguar == '*':
            num2 = int(input('=== '))
            print('')
            print(num2,'/')
            print('')
            den2 = int(input('=== '))
            print('')
            print(num2,'/',den2)
            print('')
            mult_fracc(num1, den1)
            print('')
        elif vguar == '/':
            num2 = int(input('=== '))
            print('')
            print(num2,'/')
            print('')
            den2 = int(input('=== '))
            print('')
            print(num2,'/',den2)
            print('')
            divi_fracc(num1, den1)
            print('')