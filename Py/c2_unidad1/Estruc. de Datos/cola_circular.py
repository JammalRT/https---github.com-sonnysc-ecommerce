class CircularQueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.queue = [None] * capacity
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity 
    def enqueue(self,item):
        if self.is_full():
            raise Exception("Pila llena")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
    def dequeue(self):
        if self.is_empty():
            raise Exception("Pila vacía")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
colaC = CircularQueue(6)
for elementos in [20, 10, 80, 30, 40, 90]:
    colaC.enqueue(elementos)
colaC.dequeue()
colaC.dequeue()
colaC.dequeue()
while not colaC.is_empty():
    print("Se quito el valor",colaC.dequeue())