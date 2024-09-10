#crear funcion
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

    #llamar funcion
solicitar = 'si'
while solicitar == 'si':
    print('')
    v1=input('ingrese valor: ')
    print('')
    v2=input('ingrese 2do valor: ')
    total_suma = suma (v1,v2)
    total_resta = resta (v1,v2)
    total_divicion = divicion(v1, v2)
    total_multiplicacion = multiplicacion(v1, v2)

    print('1.- Suma')
    print('2.- resta')
    print('3.- divicion')
    print('4.- multiplicacion')
    print('')
    pedir = input('Cual quieres: ')

    if pedir == '1':
        print('')
        print('la suma es',total_suma)
    elif pedir == '2':
        print('')
        print('la resta es',total_resta)
    elif pedir == '3':
        print('')
        print('la divicion es', total_divicion)
    elif pedir == '4':
        print('')
        print('la multiplicacion es', total_multiplicacion)