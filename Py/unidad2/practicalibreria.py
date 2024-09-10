nume = [1,10,20,2,0,15,150]
print(nume)
print('')
valor = int(input('ingrese el valor a encontrar: '))

posiciones = []
posicion = -1

try:
    while True:
        posiciones = nume.index(valor, posicion + 1)
        posiciones.append(posiciones)
except:
    pass 

print('')
print('La posicion es',posiciones)
print('')