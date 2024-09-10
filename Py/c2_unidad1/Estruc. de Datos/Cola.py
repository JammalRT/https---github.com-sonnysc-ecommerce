from collections import deque 
cola = deque()
cola.append('Dato 1')
cola.append('Dato 2')
cola.append('Dato 3')
cola.append('Dato 4')
print(f'Enlistar los elemntos:{cola}')
print('=================================')
while len(cola) > 0:
    elemento_siguiente = cola.popleft()
    print(f'Siguiente:{elemento_siguiente}')
    print(f'cola de imprecion: {cola}')
    print('==================================')
