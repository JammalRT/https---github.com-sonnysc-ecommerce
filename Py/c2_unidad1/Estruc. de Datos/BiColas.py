from collections import deque
#20, 10, 80, 30, 40, 90
bicola = deque()

bicola.append(20)
bicola.append(10)
bicola.appendleft(90)

print('El primer elemento de la bicola es:',bicola[0])
print('El ultimo elemento de la bicola es:',bicola[-1])

print('La cola es:',bicola)

bicola.popleft()
bicola.pop()
bicola.extend([80, 30, 40])

bicola.remove(30)

print('La cola -30:',bicola)

bicola.reverse()

print('La bicola revertida es:',bicola)

print('La cantidad de veses que aparace el numero 80 en la bicola es:', bicola.count(80))

bicola.clear()

print('la bicola esta vacia?', bicola)

