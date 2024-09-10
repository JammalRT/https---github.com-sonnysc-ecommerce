#Buqueda Lineal
def busqueda_lineal(lista, valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1
mi_lista = ['carne','pollo','pescado','lechuga','manzana','sandia','tomates','cebollas']
mi_lista2 = []
indices = []
for n in range(3):
    valor_buscado = input('Introduce el articulo a buscar: ')
    mi_lista2.append(valor_buscado)
print('========================================================')
for valor in mi_lista2:
    indice = busqueda_lineal(mi_lista, valor)
    indices.append(indice)
    if indice != -1:
        print(f'- {valor} se encuentra en el índice {indice}')
    else:
        print(f'- {valor} no está en la lista')