arreglo = []
solicitar = input('Deseas empezar a añadir elementos (s/n)')
while solicitar == 's':
    valor = input(' Agregar valor: ')
    if valor == valor in arreglo:
        arreglo.remove(valor)
        print('valor existente en el arreglo')
    arreglo.append(valor)
    solicitar = input('desea agregar otro valor? (s/n)')
print(arreglo)