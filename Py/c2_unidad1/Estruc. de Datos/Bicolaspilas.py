from collections import deque
Productos = deque()
def ingresa_producto(produ):
    Productos.append(produ)
    
def sacar_producto_viejo():
    Productos.popleft()
    
def sacar_producto_nuevo():
    Productos.pop()
    
def mostrar_inventario(produ):
    print(Productos)
    
def limpiar_peticiones():
    Productos.clear()
    
print('debes agregar 5 productos')
for i in range(5):
    produ = input('Producto que quieres agregar: ')
    ingresa_producto(produ)
    print('')

mostrar_inventario(produ)

print('')
preg = input('''Quieres borrar el producto mas viejo o el mas reciente? 
1.- reciente
2.- viejo

==== ''')
if preg == '1':
    sacar_producto_nuevo()
elif preg == '2':
    sacar_producto_viejo()
    
print('')
mostrar_inventario(produ)
print('')
limpiar_peticiones()
print('Vaciando el inventario')
print('')
print('Se a vaciado el inventario: ')
mostrar_inventario(produ)