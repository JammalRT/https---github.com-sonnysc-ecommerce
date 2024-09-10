class ColaDinamica:
    def __init__(self):
        self.items = []
        
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, item):
        self.items.append(item)
        
    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)
    
    def tamano(self):
        return len(self.items)
    
    def limpiar_ordenes(self):
        self.items.clear()
        
cola = ColaDinamica()
cola.encolar({"No. pedido": 1, "items": ["salero", "pimienta"]})
cola.encolar({"No. pedido": 2, "items": ["Playera", "Pantalones"]})
cola.encolar({"No. pedido": 3, "items": ["refrigerador", "estufa", "licuadora"]})
cola.encolar({"No. pedido": 4, "items": ["celular", "cargador"]})
cola.encolar({"No. pedido": 5, "items": ["bolsa", "gorro", "Chamarra"]})

print("Pedidos en la Fila:", cola.tamano())
print("=" * 60)

while not cola.esta_vacia():
    pedido = cola.desencolar()
    print("Desencolando pedido {} de {} artículo(s):".format(pedido["No. pedido"], len(pedido["items"])))
    for i, item in enumerate(pedido["items"], 1):
        print("{}) {}".format(i, item))
    print("-" * 60)
    print("Pedidos pendientes:", cola.tamano())
    print("=" * 60)
    
cola.limpiar_ordenes()
print("No hay más pedidos en la cola.") 