lista = [100,12,1,4,8,46,17,19,24,26,32,42,13]
busq = int(input('ingrese valor: '))
lista_ordenada = sorted(lista)
print(lista_ordenada)
primero = 0
ultimo = len(lista_ordenada) -1
encontrado = False

while primero <= ultimo and not encontrado:
    punto_medio = int((primero + ultimo) / 2)
    if punto_medio == busq:
        print('encontrado')
        encontrado = True
    else:
        if busq < lista_ordenada[punto_medio]:
            ultimo = punto_medio - 1
        else:
            primero = punto_medio + 1
print('Encontrado el valor : '+ str(busq) + ' en la posicion '+ str(punto_medio))