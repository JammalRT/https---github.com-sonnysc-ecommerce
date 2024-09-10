import random # Importa el módulo random para generar números aleatorios

nums = [] # Crea una lista vacía llamada nums

# Define la función busqueda_binaria que toma dos argumentos: una lista nums y un valor_buscado que se busca en la lista
def busqueda_binaria(nums, valor_buscado):
    izquierda= 0 # Define un índice izquierda que apunta al primer elemento de la lista
    derecha = len(nums)-1 # Define un índice derecha que apunta al último elemento de la lista
    while izquierda <= derecha: # Mientras izquierda sea menor o igual a derecha
        medio = (izquierda + derecha)//2 # Calcula el índice del elemento medio de la lista
        if nums[medio] == valor_buscado: # Si el elemento medio de la lista es igual al valor buscado
            return medio # Devuelve el índice del elemento medio
        elif nums[medio] < valor_buscado: # Si el elemento medio de la lista es menor que el valor buscado
            izquierda = medio + 1 # Actualiza el índice izquierda para excluir los elementos de la izquierda del medio
        else: # Si el elemento medio de la lista es mayor que el valor buscado
            derecha = medio - 1 # Actualiza el índice derecha para excluir los elementos de la derecha del medio
    return -1 # Devuelve -1 si el valor buscado no se encuentra en la lista

# Genera 99 números aleatorios únicos en el rango de 1 a 100 y los agrega a la lista nums
while len(nums) < 99:
    nums_ran = random.randint(0, 99)
    if nums_ran not in nums:
        nums.append(nums_ran)       

nums_ord = sorted(nums) # Ordena la lista nums en orden ascendente y la guarda en la variable nums_ord
print(nums_ord) # Imprime la lista nums_ord
valor_buscado = int(input('Que numero quieres buscar? ')) # Pide al usuario que ingrese un número para buscar en la lista
indice = busqueda_binaria(nums_ord, valor_buscado) # Busca el número ingresado por el usuario en la lista nums_ord usando la función busqueda_binaria

# Si el número buscado se encuentra en la lista, imprime su índice (posición) en la lista
if indice != -1:
    print(f"El número {valor_buscado} se encuentra en la posición {indice}.")
else: # Si el número buscado no se encuentra en la lista, imprime un mensaje indicando que no se encontró
    print(f"El número {valor_buscado} no se encuentra en la lista.")