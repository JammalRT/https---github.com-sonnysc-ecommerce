import random
# Función que implementa el método de ordenamiento por inserción
def insertion_sort(array):
    # Se itera sobre todos los elementos del arreglo
    for i in range(1, len(array)):
        elem = array[i] # Se toma el elemento actual como "clave"
        j = i - 1
        # Se mueven los elementos mayores que la clave una posición hacia adelante
        while j >= 0 and array[j] > elem:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = elem # Se inserta la clave en su posición correcta
        print("-------------------------------------")
        print(arr)
# arreglo de tamaño variable y llenado con valores aleatorios
arr = [random.randint(0, 100) for i in range(10)]
print("")
print("Arreglo Original: ")
print(arr)
print("")
insertion_sort(arr)
print("------------------------------------------")
print("")
print("Arreglo Ordenado: ")
print(arr)
print("")