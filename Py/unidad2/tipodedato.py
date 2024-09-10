arreglo = [str, int, bool, float]
arreglo2 = ['algoritmos', 1, True,5.00,'c', 'Reprobados']
for tipo in arreglo:
    print(tipo)
    for dato in arreglo2:
        print(type(dato) == tipo, end=' ')
        print('')