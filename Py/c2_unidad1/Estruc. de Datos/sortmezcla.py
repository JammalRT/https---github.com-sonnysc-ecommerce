def merge_sort(arr):
    # Comprobamos si la longitud de la lista es mayor que 1, es decir, si hay elementos que ordenar
    if len(arr) > 1:
        # Dividimos la lista en dos mitades
        mid = len(arr) // 2
        mitad_izq = arr[:mid]
        mitad_der = arr[mid:]
        # Ordenamos cada mitad
        merge_sort(mitad_izq)
        merge_sort(mitad_der)
        # Combinamos las dos mitades ordenadas en una sola lista
        i = j = k = 0  # índices para recorrer la lista
        while i < len(mitad_izq) and j < len(mitad_der):
            if mitad_izq[i] < mitad_der[j]:
                arr[k] = mitad_izq[i]
                i += 1
            else:
                arr[k] = mitad_der[j]
                j += 1
            k += 1
        # Agregamos cualquier elemento restante de las dos mitades
        while i < len(mitad_izq):
            arr[k] = mitad_izq[i]
            i += 1
            k += 1
        while j < len(mitad_der):
            arr[k] = mitad_der[j]
            j += 1
            k += 1
        # Imprimimos la lista después de cada iteración para observar el proceso
        print(arr)
        
# Ejecucion del metodo
arr = [70, 52, 80, 12, 17, 89, 97, 60]
print("Metodo de mezcla")
print("================================")
merge_sort(arr)