from NodosG import *
class Grafo:

    def __init__(self):
        self.nodos = {}     # diccionario "HashTable"
        self.aristas = []   # lista
        self.adjacency_list = {}  # new attribute

    def get_neighbors(self, node):
        return self.adjacency_list[node]

    def agregar_nodo(self, nodo):
        self.nodos[nodo.id] = nodo
        self.adjacency_list[nodo.id] = []  # initialize the adjacency list for the node

    def agregar_arista(self, nodo_inicio, nodo_destino, distancia, calle):
        if nodo_inicio.id in self.nodos and nodo_destino.id in self.nodos:
            arista = Arista(nodo_inicio, nodo_destino, distancia, calle)
            self.aristas.append(arista)
            # update the adjacency list
            self.adjacency_list[nodo_inicio.id].append((nodo_destino.id, calle, distancia))  # include the distance


    def mostrar_grafo(self):
        n = len(self.aristas)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.aristas[j].peso > self.aristas[j + 1].peso:
                    self.aristas[j], self.aristas[j + 1] = self.aristas[j + 1], self.aristas[j]
        for arista in self.aristas:
            print(f"{arista}")