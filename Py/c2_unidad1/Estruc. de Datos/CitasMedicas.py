class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.siguiente = None
        
class ColaDinamica:
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.tamano=0
        
    def enqueue (self, valor):
        nuevo_nodo=Nodo (valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola= nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1
                
    def dequeue(self):
        if self.cabeza is None:
            return None
        valor= self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        self.tamano -= 1
        return valor
        
    def front(self):
        if self.cabeza is None:
            return None 
        return self.cabeza.valor
    
    def is_empty(self):
        return self.cabeza is None
        
    def size (self):
        return self.tamano 
        
pregunta = input("Desea agregar una cita (si/no): ")
if pregunta == 'si':
    pregunta2=int(input('''Que dia desea realizar su cita el 
- 15 
- 20
- 25
======: '''))
    cola=ColaDinamica()
    if pregunta2 == 15:
        cola.enqueue(15)
    elif pregunta2 == 20:
        cola.enqueue(20)
    elif pregunta2 == 25:
        cola.enqueue(25)
    cola.enqueue(10)
    cola.enqueue(8)
    cola.enqueue(7)
    pregunta3=input("Deseas eliminar tu cita si/no? ")
    if pregunta3 == "si":
        cola.is_empty()
        valor=cola.dequeue()
        print("Se elimino el dia : ",valor)
    else:
        print("==================================")
    print("Las citas que hay son ", cola.size())
    print("==================================")
    print("Primera persona que sera atendida sera el dia : ",cola.front())
    while not cola.is_empty():
        valor=cola.dequeue()
        print("Persona que ya fue atendita: ",valor)
    print("==================================")   
    print("Pacientes por atender ",cola.size())
    

print('==================================')
print('')
print('Gracias Por Su Visita :D')
print('')
print('==================================')
    
