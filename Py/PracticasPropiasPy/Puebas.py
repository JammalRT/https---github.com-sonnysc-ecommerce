#BUSQUEDA INTERPOLACION
num = [1, 2, 3, 5, 6, 8, 9, 11, 13, 14, 15]
def busqueda_interpolacion(lista, objetivo):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo and objetivo >= lista[minimo] and objetivo <= lista[maximo]:
        posicion = minimo + (maximo - minimo) * (objetivo - lista[minimo]) // (lista[maximo] - lista[minimo])
        if lista[posicion] == objetivo:
            return posicion  
        elif objetivo < lista[posicion]:
            maximo = posicion - 1
        else:
            minimo = posicion + 1
    return -1 
objetivo = 6
indice = busqueda_interpolacion(num, objetivo)
if indice != -1:
    print(f"El número {objetivo} se encuentra en la posición {indice} de la lista.")
else:
    print(f"El número {objetivo} no está en la lista.")