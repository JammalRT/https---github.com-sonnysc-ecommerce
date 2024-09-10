arreglo = ['',]
agregar = input('Desea agregar dias? (s/n) ')
while agregar == 's':
    semana = str(input('Escribe un dia de la semana: '))
    arreglo.append(semana)
    agregar = input('Desea agregar mas dias? (s/n) ')
    print('')
print(arreglo)

dia = str(input('Escribe el numero del dia del que quieras saber su posicion: '))
indice = arreglo.index(dia)
print('la posicion del', dia, 'es', indice)
print('')