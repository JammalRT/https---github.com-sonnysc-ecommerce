def busqueda_lineal(lista, valor_buscado):

    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1
        
mi_Lista = ["Carne", "Pollo", "Pescado", "Lechuga", "Manzana", "Sandia", "Tomate", "Cebollas"]
print(" ")
pregunta = "si"

while pregunta == "si":
    valor_buscado = input("Introduzca el producto que desea buscar en su lista: ")

    indice = busqueda_lineal(mi_Lista, valor_buscado)

    if indice != -1:
        print(f"El valor {valor_buscado} se encuentra en el indice {indice}.")
        print("")
    else:
        print(f"El valor {valor_buscado} no se encuentra en la lista.")
        print("")
    
    pregunta = input("¿Desea saber otro producto? ")
    print("")