def busqueda_binaria(lista_ordenada, valor):
    pasos = 0
    izq = 0
    der = len(lista_ordenada) - 1 
    while izq <= der:
        pasos += 1
        punto_medio = (izq + der)//2
        if lista_ordenada[punto_medio] == valor:
            return 'valor encontrado en {} pasos, en la posicion {}'.format(pasos, punto_medio)
        if lista_ordenada[punto_medio] > valor:
            der = punto_medio - 1 
        if lista_ordenada[punto_medio] < valor:
            izq = punto_medio + 1
    return 'elemento no enontrado' 

def busqueda_secuencial(lista_ordenada):
    solisitar = 'si'
    while solisitar == 'si':
        print('')
        bus = int(input('Posicion en busqueda secuencial: '))
        print('')
        indice = lista_ordenada.index(bus)
        print('Secuencial')
        print('')
        print('la posicion del', bus, 'es', indice)
        print('')
lista = []
solisitar = 'si'
while solisitar == 'si':
    agre = int(input('agrega los datos al arreglo: '))
    lista.append(agre)
    solisitar = input('quiere agreagar mas datos? (si/no) ')
    lista_ordenada = sorted(lista)
print(lista_ordenada)
print('')

solisitar = 'si'
while solisitar == 'si':   
    izq = 0
    der = len(lista_ordenada) - 1
    punto_medio = (izq + der)//2
    print('')
    val = input('Valor de busqueda binaria: ')
    print('')
    print('binaria')
    print('')
    if val == punto_medio:
        posicion = busqueda_binaria(lista_ordenada, int(val))
        print(posicion)
    else:
        posicion = busqueda_binaria(lista_ordenada, int(val))
        print(posicion)
        busqueda_secuencial(lista_ordenada)
      
busqueda_secuencial(lista_ordenada)