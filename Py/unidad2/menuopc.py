resp = 's'
while resp == 's':
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
    print('1.- Suma')
    print('2.- resta')
    print('3.- divicion')
    print('4.- multiplicacion')
    print('')
    v1=input('ingrese valor: ')
    print('')
    v2=input('ingrese 2do valor: ')
    print('')
    total_suma = suma (v1,v2)
    total_resta = resta (v1,v2)
    total_divicion = divicion(v1, v2)
    total_multiplicacion = multiplicacion(v1, v2)

    print('1.- Suma')
    print('2.- resta')
    print('3.- divicion')
    print('4.- multiplicacion')
    print('')
    pedir = input('Que operacion quiere: ')
    print('')

    if pedir == '1':
        print('la suma es',total_suma)
        print('')
    elif pedir == '2':
        print('la resta es',total_resta)
        print('')
    elif pedir == '3':
        print('la divicion es', total_divicion)
        print('')
    elif pedir == '4':
        print('la multiplicacion es', total_multiplicacion)
        print('')