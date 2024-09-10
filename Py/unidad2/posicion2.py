lista = [54,87,3,2,9,8,46,13,79,56,15,55,79,61]
valor = int(input('ingrese valor: '))
encontrado = False
pos = 0
while pos < len(lista) and not encontrado:
    if lista[pos] == valor:
        print(valor, ' encontradoo en la posicion ' + str(pos))
        encontrado = True
    else:
        pos = pos + 1 
        print('no encontrado')