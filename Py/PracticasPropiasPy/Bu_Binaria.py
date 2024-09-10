def Busqueda_Binario(lista, valor_buscado):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor_buscado:
            return medio
        elif lista[medio] < valor_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
precios = [10.50, 11.25, 12.75, 14.00, 15.50, 16.75, 18.25]
valores_buscados = []
indices = []
for i in range(3):
    valor_buscado = float(input('Introduce el precio a buscar: '))
    valores_buscados.append(valor_buscado)
for valor in valores_buscados:
    indice = Busqueda_Binario(precios, valor)
    if indice != -1:
        indices.append(indice)
    else:
        print(f'El valor {valor} no se encuentra en la lista.')
print('=========================================================')
for i in range(len(valores_buscados)):
    valor = valores_buscados[i]
    indice = indices[i]
    print(f'{valor} se encuentra en el índice {indice}')