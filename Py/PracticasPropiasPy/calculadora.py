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

print('')
print('CALCULADORA CASTIO')
print('')
print('=================================================================================================================')
print('')
v1 = input('Ingresa el primer valor: ')
resultados.update({'resultado':v1})
sol = 'si'
while sol == 'si':
    v1 = resultados['resultado']
    print('')
    print('''1.-Suma
2.-Resta
3.-Multiplicacion
4.-Divicion
''')
    vguar = input('que operacion deseas hacer: ')
    print('')
    if vguar == '1':
        print('Suma',v1,'con: ')
        print('')
        v2 = input('Ingresa el segundo valor: ')
        print('')
    elif vguar == '2':
        print('Resta',v1,'con: ')
        print('')
        v2 = input('Ingresa el segundo valor: ')
        print('')
    elif vguar == '3':
        print('Multiplica',v1,'con: ')
        print('')
        v2 = input('Ingresa el segundo valor: ')
        print('')
    elif vguar == '4':
        print('Divide',v1,'entre: ')
        print('')
        v2 = input('Ingresa el segundo valor: ')
        print('')
        
    total_suma = suma (v1,v2)
    total_resta = resta (v1,v2)
    total_divicion = divicion(v1, v2)
    total_multiplicacion = multiplicacion(v1, v2)
    
    if vguar == '1':
        print(total_suma)
        res = total_suma
    elif vguar == '2':
        print(total_resta)
        res = total_resta
    elif vguar == '3':
        print(total_multiplicacion)
        res = total_multiplicacion
    elif vguar == '4':
        print(total_divicion)
        res = total_divicion
    
    resultados.update({'resultado':res})