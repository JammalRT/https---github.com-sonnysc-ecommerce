def insertion_sort(arr):
    # Obtenemos la longitud de la lista
    n = len(arr)
    # Recorremos la lista, comenzando desde el segundo elemento
    for i in range(1, n):
        # Almacenamos el elemento actual en una variable temporal
        elem = arr[i]
        # Comparamos el elemento actual con los elementos anteriores en la lista
        # y los desplazamos hacia la derecha si son mayores que el elemento actual
        j = i - 1
        while j >= 0 and elem < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # Insertamos el elemento actual en la posición correcta en la lista
        arr[j+1] = elem
        # Imprimimos la lista después de cada iteración para observar el proceso
        print(arr)

# Ejecucion del metodo
arr = [31, 1, 84, 14, 22, 14, 27]
print("Metodo de insercion")
print("================================")
insertion_sort(arr)