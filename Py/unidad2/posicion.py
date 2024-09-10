nume = [1,10,20,2,0,15,150]
encontrado = False 
pos = 0 
valor = input('ingrese el valor ')
while not encontrado:
    if nume(pos) == valor:
        print()
        encontrado = True
    else:
        pos = pos+1 