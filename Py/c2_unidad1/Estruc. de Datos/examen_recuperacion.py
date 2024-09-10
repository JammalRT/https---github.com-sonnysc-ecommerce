# Definimos la función de búsqueda binaria
def busqueda_binaria(arr, x):
    n = len(arr)
    inicio = 0
    fin = n - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        # Si el elemento que buscamos es el medio, lo encontramos
        if arr[medio] == x:
            # Retornamos el índice del elemento encontrado, el valor en sí,
            # y los valores de los elementos previo y siguiente en la lista
            return medio, arr[medio], arr[medio-1], arr[medio+1]
        # Si el elemento buscado es mayor que el medio, buscamos en la mitad superior de la lista
        elif arr[medio] < x:
            inicio = medio + 1
        # Si el elemento buscado es menor que el medio, buscamos en la mitad inferior de la lista
        else:
            fin = medio - 1
    # Si no encontramos el elemento, retornamos -1 y valores nulos para los otros parámetros
    return -1, None, None, None

# Definimos la función de ordenamiento por selección
def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n):
        # Encontramos el elemento mínimo en la sublista restante
        minimo = i
        for j in range(i+1, n):
            if arr[j] < arr[minimo]:
                minimo = j
        # Intercambiamos el elemento mínimo con el primer elemento de la sublista
        arr[i], arr[minimo] = arr[minimo], arr[i]
    # Retornamos la lista ordenada
    return arr

# Creamos una lista vacía para almacenar las temperaturas
temperaturas = []
# Pedimos al usuario que ingrese las temperaturas y las agregamos a la lista
while True:
    temperatura = input("""Ingrese una temperatura: 
o escribe 'fin' para terminar: """)
    if temperatura == "fin":
        break
    try:
        temperatura = int(temperatura)
        temperaturas.append(temperatura)
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")

# Ordenamos la lista de temperaturas utilizando la función de ordenamiento por selección
temperaturas = ordenamiento_seleccion(temperaturas)
print("Temperaturas ordenadas:", temperaturas)

# Pedimos al usuario que ingrese la temperatura que está buscando
temperatura_objetivo = int(input("Ingrese la temperatura que está buscando: "))
# Buscamos la temperatura objetivo utilizando la función de búsqueda binaria
indice, temperatura, grado_anterior, grado_siguiente = busqueda_binaria(temperaturas, temperatura_objetivo)
# Imprimimos los resultados de la búsqueda
if indice == -1:
    print("La temperatura no se encontró en la lista.")
else:
    print(f"Temperatura objetivo: {temperatura}")
    print(f"Índice en el que se encuentra: {indice}")
    if grado_anterior is not None:
        print(f"Grado inicio: {grado_anterior}")
    if grado_siguiente is not None:
        print(f"Grado fin: {grado_siguiente}")