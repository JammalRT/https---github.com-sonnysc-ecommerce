# Declaramos el arreglo
arreglo = []
# Declaramos la variable solisitar
solicitar = input('Desea iniciar el proceso (s/n)')
while solicitar == 's':
    # Ingresamos los valores a sumar
    valor1 = input('ingresa el valor ')
    valor2 = input('ingresa el segundo valor ') 
    # Sumamos los valores 
    total = int(valor1) + int(valor2)
    print('')
    print('El total es =', (total))
    print('')
    if total == total in arreglo:
        print('ya existe en el arreglo')
        print('')
        arreglo.remove(total)
    # Agregamos el resultado al arreglo
    arreglo.append(total)
    solicitar = input('Desea agregar mas datos? (s/n)')
print(arreglo)