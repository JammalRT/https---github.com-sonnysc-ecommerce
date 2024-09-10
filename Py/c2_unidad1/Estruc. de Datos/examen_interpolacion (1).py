def busqueda_interpolacion(arr, x):
    n = len(arr)
    inicio = 0
    fin = n - 1
    while inicio <= fin and x >= arr[inicio] and x <= arr[fin]:
        pos = inicio + ((x - arr[inicio]) * (fin - inicio)) // (arr[fin] - arr[inicio])
        if arr[pos] == x:
            return pos, arr[pos], arr[pos-1], arr[pos+1]
        if arr[pos] < x:
            inicio = pos + 1
        else:
            fin = pos - 1
    return -1, None, None, None
temperaturas = []
for i in range(10):
    temperatura = int(input(f"Ingrese la temperatura {i+1}: "))
    temperaturas.append(temperatura)
temperaturas.sort()
print(temperaturas)
inicio = temperaturas[0]
fin = temperaturas[-1]
temperatura_objetivo = int(input("Ingrese la temperatura que está buscando: "))
indice, temperatura, grado_anterior, grado_siguiente = busqueda_interpolacion(temperaturas, temperatura_objetivo)
if indice == -1:
    print("La temperatura no se encontró en la lista.")
else:
    print(f"Temperatura objetivo: {temperatura}")
    print(f"Índice en el que se encuentra: {indice}")
    if grado_anterior is not None:
        print(f"Grado inicio: {inicio}")
    if grado_siguiente is not None:
        print(f"Grado fin: {fin}")