class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
class Pila:
    def __init__(self):
        self.superior=None
    def push(self, dato):
        print(f"Agregando {dato} en la cima de la pila")
        if self.superior==None:
            self.superior=Nodo(dato)
            return
        nuevo_nodo=Nodo(dato)
        nuevo_nodo.siguiente=self.superior
        self.superior=nuevo_nodo
    def pop(self):
        if self.superior==None:
            print("++++++No hay ningun elemento de la pila para desapilar+++++++")
            return
        print(f"Desapilar: {self.superior.dato}")
        self.superior=self.superior.siguiente
    def imprimir(self):
        print("++++++Imprimiendo pila++++++")
        nodo_temporal=self.superior
        while nodo_temporal !=None:
            print(f"{nodo_temporal.dato}",end=",")
            nodo_temporal=nodo_temporal.siguiente
        print("")
pila = Pila()
pila.push('Jammal')
pila.push('Kevin')
pila.push('Jonathan')
pila.push('Raymundo')
pila.push('Estefania')
pila.imprimir()
pila.pop()
pila.pop()
pila.pop()
pila.pop()
pila.pop()
pila.imprimir()
#201080304090