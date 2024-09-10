import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz)

    def agregar_nodo(self, valor, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self.agregar_nodo(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self.agregar_nodo(valor, nodo_actual.derecha)

    def recorrer_inorden(self, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if nodo_actual.izquierda is not None:
            self.recorrer_inorden(nodo_actual.izquierda)

        print(nodo_actual.valor)

        if nodo_actual.derecha is not None:
            self.recorrer_inorden(nodo_actual.derecha)
            
    def recorrer_preorden(self, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        print(nodo_actual.valor)

        if nodo_actual.izquierda is not None:
            self.recorrer_preorden(nodo_actual.izquierda)

        if nodo_actual.derecha is not None:
            self.recorrer_preorden(nodo_actual.derecha)
            
    def recorrer_posorden(self, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        if nodo_actual.izquierda is not None:
            self.recorrer_posorden(nodo_actual.izquierda)

        if nodo_actual.derecha is not None:
            self.recorrer_posorden(nodo_actual.derecha)

        print(nodo_actual.valor)
        
    def dibujar_arbol(self):
        G = nx.DiGraph()
        self._crear_grafo(self.raiz, G)

        pos = nx.spring_layout(G)

        labels = {}
        for node in G.nodes():
            labels[node] = node.valor
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color='blue')
        nx.draw_networkx_edges(G, pos, arrows=True)
        nx.draw_networkx_labels(G, pos, labels)
        plt.show()

    def _crear_grafo(self, nodo_actual, G):
        if nodo_actual is not None:
            G.add_node(nodo_actual)
            if nodo_actual.izquierda is not None:
                G.add_edge(nodo_actual, nodo_actual.izquierda)
                self._crear_grafo(nodo_actual.izquierda, G)
            if nodo_actual.derecha is not None:
                G.add_edge(nodo_actual, nodo_actual.derecha)
                self._crear_grafo(nodo_actual.derecha, G)

if __name__ == '__main__':
    valor_raiz = int(input("Ingrese el valor de la raíz: "))
    arbol = ArbolBinario(valor_raiz)

    while True:
        valor = input("Ingrese el valor del nodo o ingrese 'e' para terminar: ")
        if valor.__eq__('e'):
            break
        if valor.isnumeric():
            arbol.agregar_nodo(int(valor))
        else:
            print('El valor no es numerico')
        
    print('-- Recorrido Inorden --')
    arbol.recorrer_inorden()
    print('-- Recorrido Preorden --')
    arbol.recorrer_preorden()
    print('-- Recorrido Posorden --')
    arbol.recorrer_posorden()

    arbol.dibujar_arbol()