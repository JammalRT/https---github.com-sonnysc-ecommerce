import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Nodo:
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
        self.nodos_vecinos = []

    def agregar_vecino(self, nodo, peso):
        self.nodos_vecinos.append((nodo, peso))

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

    def obtener_nodo_por_id(self, id):
        for nodo in self.nodos:
            if nodo.id == id:
                return nodo
        return None

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

    def dijkstra(self, origen_id):
        distancias = {nodo.id: float('inf') for nodo in self.nodos}
        distancias[origen_id] = 0

        heap = [(0, origen_id)]
        nodos_previos = {}

        while heap:
            distancia_actual, nodo_actual_id = heapq.heappop(heap)

            if distancia_actual > distancias[nodo_actual_id]:
                continue

            nodo_actual = self.obtener_nodo_por_id(nodo_actual_id)

            for vecino, peso in nodo_actual.nodos_vecinos:
                distancia = distancias[nodo_actual_id] + peso

                if distancia < distancias[vecino.id]:
                    distancias[vecino.id] = distancia
                    nodos_previos[vecino.id] = nodo_actual.id
                    heapq.heappush(heap, (distancia, vecino.id))

        return nodos_previos

    def obtener_camino(self, origen_id, destino_id):
        nodos_previos = self.dijkstra(origen_id)
        camino = []
        actual = destino_id

        while actual != origen_id:
            camino.append(actual)
            actual = nodos_previos[actual]

        camino.append(origen_id)
        camino.reverse()

        return camino

grafo = Grafo()

cantidad_nodos = int(input("Ingrese la cantidad de nodos del grafo: "))

for i in range(1, cantidad_nodos + 1):
    valor_nodo = input(f"Ingrese el valor del nodo {i}: ")
    nodo = Nodo(i, valor_nodo)
    grafo.agregar_nodo(nodo)

cantidad_aristas = int(input("Ingrese la cantidad de aristas del grafo: "))

for i in range(1, cantidad_aristas + 1):
    peso_arista = float(input(f"Ingrese el peso de la arista {i}: "))

    origen_id = int(input(f"Ingrese el id del nodo origen de la arista {i}: "))
    destino_id = int(input(f"Ingrese el id del nodo destino de la arista {i}: "))

    nodo_origen = grafo.obtener_nodo_por_id(origen_id)
    nodo_destino = grafo.obtener_nodo_por_id(destino_id)

    arista = Arista(i, peso_arista, nodo_origen, nodo_destino)
    grafo.agregar_arista(arista)

    nodo_origen.agregar_vecino(nodo_destino, peso_arista)
    
print(grafo)

origen_id = int(input("Ingrese el id del nodo origen para el algoritmo de Dijkstra: "))

nodos_previos = grafo.dijkstra(origen_id)

for nodo_id, previo_id in nodos_previos.items():
    if nodo_id != origen_id:
        camino = grafo.obtener_camino(origen_id, nodo_id)
        distancia = sum(grafo.obtener_nodo_por_id(camino[i]).nodos_vecinos[j][1] for i in range(len(camino)-1) for j in range(len(grafo.obtener_nodo_por_id(camino[i]).nodos_vecinos)) if grafo.obtener_nodo_por_id(camino[i]).nodos_vecinos[j][0].id == grafo.obtener_nodo_por_id(camino[i+1]).id)
        print(f"Distancia desde el nodo {origen_id} al nodo {nodo_id}: {distancia}")
        print(f"Camino más corto: {' -> '.join(str(nodo) for nodo in camino)}")
        print()
        
grafo.dibujar_grafo()