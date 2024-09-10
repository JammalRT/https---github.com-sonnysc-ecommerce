import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    '''
    Clase Nodo que me ayuda a generar los nodos del árbol
    '''
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
                nodo_actual.izquierda = Nodo(valor) # type: ignore
            else:
                self.agregar_nodo(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor) # type: ignore
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

if __name__ == '__main__':
    arbol = ArbolBinario(10)
    arbol.agregar_nodo(5)
    arbol.agregar_nodo(15)
    arbol.agregar_nodo(3)
    arbol.agregar_nodo(7)
    arbol.agregar_nodo(12)
    arbol.agregar_nodo(20)

    print('-- Recorrido Inorden --')
    arbol.recorrer_inorden()
    print('-- Recorrido Preorden --')
    arbol.recorrer_preorden()
    print('-- Recorrido Posorden --')
    arbol.recorrer_posorden()

