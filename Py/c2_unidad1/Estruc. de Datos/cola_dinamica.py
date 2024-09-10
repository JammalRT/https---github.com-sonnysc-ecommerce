class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
cola = Cola()
cola.enqueue(20)
cola.enqueue(10)
cola.enqueue(80)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(90)
print('El elemnto en la cola:',cola.size())
print('=================================')
print('Primer elemento:')
print('=================================')
while not cola.is_empty():
    valor = cola.dequeue()
    print('Valor eliminado:',valor)
print('=================================')
print('elementos de la cola:',cola.size())