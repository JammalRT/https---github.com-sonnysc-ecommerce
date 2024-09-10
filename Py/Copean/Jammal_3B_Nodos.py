import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
        self.nodos_vecinos = []

    def agregar_vecino(self, nodo):
        self.nodos_vecinos.append(nodo)

    def __str__(self):
        return f"Nodo {self.id}: {self.valor}"

class Arista:
    def __init__(self, id, peso, origen, destino):
        self.id = id
        self.peso = peso
        self.origen = origen
        self.destino = destino

    def __str__(self):
        return f"Arista {self.id}: Peso={self.peso}, Origen={self.origen.id}, Destino={self.destino.id}"

class Grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def agregar_arista(self, arista):
        self.aristas.append(arista)

    def __str__(self):
        nodos_str = "\n".join(str(nodo) for nodo in self.nodos)
        aristas_str = "\n".join(str(arista) for arista in self.aristas)
        return f"Grafo:\nNodos:\n{nodos_str}\nAristas:\n{aristas_str}"

    def dibujar_grafo(self):
        G = nx.Graph()

        for nodo in self.nodos:
            G.add_node(nodo.id, label=nodo.valor)

        for arista in self.aristas:
            G.add_edge(arista.origen.id, arista.destino.id, weight=arista.peso)

        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')
        edge_labels = nx.get_edge_attributes(G, 'weight')

        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, labels, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

        plt.axis('off')
        plt.show()

grafo = Grafo()

cantidad_nodos = int(input("Ingrese la cantidad de nodos del grafo: "))

for i in range(1, cantidad_nodos + 1):
    valor_nodo = input(f"Ingrese el valor del nodo {i}: ")
    nodo = Nodo(i, valor_nodo)
    grafo.agregar_nodo(nodo)

cantidad_aristas = int(input("Ingrese la cantidad de aristas del grafo: "))

for i in range(1, cantidad_aristas + 1):
    peso_arista = int(input(f"Ingrese el peso de la arista {i}: "))

    origen_id = int(input(f"Ingrese el id del nodo origen de la arista {i}: "))
    destino_id = int(input(f"Ingrese el id del nodo destino de la arista {i}: "))

    nodo_origen = None
    nodo_destino = None
    for nodo in grafo.nodos:
        if nodo.id == origen_id:
            nodo_origen = nodo
        elif nodo.id == destino_id:
            nodo_destino = nodo

    arista = Arista(i, peso_arista, nodo_origen, nodo_destino)
    grafo.agregar_arista(arista)

    nodo_origen.agregar_vecino(nodo_destino)

print(grafo)

grafo.dibujar_grafo()