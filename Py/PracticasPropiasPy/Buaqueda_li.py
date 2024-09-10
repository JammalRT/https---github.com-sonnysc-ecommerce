#Buqueda Lineal
def busqueda_lineal(lista, valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1
mi_lista = [20,10,80,30,40,90]
valor_buscado = int(input('introduce el valor a buscar: '))
indice = busqueda_lineal(mi_lista, valor_buscado)
if indice != -1:
    print(f'El valor {valor_buscado} se encuentra en el indice {indice}')
else:
    print(f'El valor {valor_buscado} no se encuentra en la lista.')