# Definimos la estructura de datos tipo cola dinámica
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
# Recolectamos los datos climatológicos
queue = Queue()
temperatures = [15, 20, 23, 17, 25, 19, 16, 22, 21, 18]
for temperature in temperatures:
    queue.enqueue(temperature)
# Ordenamos la estructura por medio del método de selección
for i in range(queue.size()):
    min_index = i
    for j in range(i+1, queue.size()):
        if queue.items[j] < queue.items[min_index]:
            min_index = j
    queue.items[i], queue.items[min_index] = queue.items[min_index], queue.items[i]
    print(queue.items)
# Buscamos el elemento por medio del método binario
def binary_search(queue, item):
    start = 0
    end = queue.size() - 1
    while start <= end:
        mid = (start + end) // 2
        if queue.items[mid] == item:
            return mid, queue.items[0], queue.items[-1]
        elif queue.items[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return -1, None, None
# Solicitamos al usuario la temperatura a buscar
temperature_to_find = int(input("Introduce la temperatura que buscas: "))
# Ejecutamos la búsqueda binaria y mostramos los resultados
index, start, end = binary_search(queue, temperature_to_find)
if index == -1:
    print(f"La temperatura {temperature_to_find} no se encuentra en la estructura.")
else:
    print(f"La temperatura {temperature_to_find} se encuentra en el índice {index} y está entre {start} y {end}.")