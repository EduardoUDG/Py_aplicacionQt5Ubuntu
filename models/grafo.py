from arista import Arista
from collections import deque
from nodo import Nodo
from queue import PriorityQueue


class Grafo:
    def __init__(self) -> None:
        self.__aristas = []
        self.__ady = {}  # dict()
        self.__adyPonderado = {}

    def agregar_arista(self, arista: Arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)

    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])

    def eliminar_arista(self, arista: Arista):
        self.__aristas.remove(arista)

    def get_lista_ady(self) -> dict:
        self.__ady.clear()

        for arista in self.__aristas:
            if arista.dirigido():
                pass
            else:
                n1 = arista.get_nodo1()
                n2 = arista.get_nodo2()
                self.agregar_dict(n1, n2)
                self.agregar_dict(n2, n1)
        return self.__ady

    def print_ady(self):
        self.get_lista_ady()
        for key in self.__ady.keys():
            print(key, "---->", end="")
            for value in self.__ady[key]:
                nodo = value[0]
                print(nodo, end="")
            print('\n')

    def mostrar_ady(self):
        self.get_lista_ady()
        string = ""
        for key in self.__ady.keys():
            string += str(key) + "---->"
            for value in self.__ady[key]:
                nodo = value[0]
                string += str(nodo)
            string += '\n'
        return string

    def agregar_dict(self, n1, n2):
        if n1 in self.__ady:
            self.__ady[n1].append([n2])
        else:
            self.__ady[n1] = [[n2]]

    def recorrido_profundidad(self, inicio: Nodo):
        visitados = []
        pila = deque()
        recorrido = []

        grafo = self.get_lista_ady()

        if inicio not in grafo:
            return recorrido

        pila.append(inicio)
        visitados.append(inicio)

        while len(pila) > 0:
            nodo = pila.pop()
            recorrido.append(nodo)

            for ady in grafo[nodo]:
                if ady[0] not in visitados:
                    pila.append(ady[0])
                    visitados.append(ady[0])

        return recorrido

    def recorrido_amplitud(self, inicio: Nodo):
        visitados = []
        cola = deque()
        recorrido = []

        grafo = self.get_lista_ady()

        if inicio not in grafo:
            return recorrido

        cola.append(inicio)
        visitados.append(inicio)

        while len(cola) > 0:
            vertice = cola.popleft()
            recorrido.append(vertice)

            for ady in grafo[vertice]:
                if ady[0] not in visitados:
                    cola.append(ady[0])
                    visitados.append(ady[0])

        return recorrido

##### Funciones para AristaNoDirigidaPonderada #####

    def get_lista_ady_ponderada(self) -> dict:
        self.__adyPonderado.clear()

        for arista in self.__aristas:
            if arista.dirigido():
                pass
            else:
                n1 = arista.get_nodo1()
                n2 = arista.get_nodo2()
                self.agregar_dict_ponderado(n1, n2, arista.peso)
                self.agregar_dict_ponderado(n2, n1, arista.peso)
        return self.__adyPonderado

    def print_ady_ponderada(self):
        self.get_lista_ady_ponderada()
        for key in self.__adyPonderado.keys():
            print(key, "---->", end="")
            for value in self.__adyPonderado[key]:
                nodo = value[0]
                peso = value[1]
                print(f"[{nodo}, {peso}]", ",", end="")
            print('\n')

    def agregar_dict_ponderado(self, n1, n2, peso):
        if n1 in self.__adyPonderado:
            self.__adyPonderado[n1].append([n2, peso])
        else:
            self.__adyPonderado[n1] = [[n2, peso]]

    def prim(self, inicio: Nodo):
        grafo_resultante = []
        visitados = []
        pq = PriorityQueue()

        visitados.append(inicio)

        for ady in self.__adyPonderado[inicio]:
            arista = (ady[1], inicio, ady[0])
            pq.put(arista)

        while not pq.empty():
            arista = pq.get()
            # print('Arista: ', arista)
            destino = arista[2]
            if destino not in visitados:
                visitados.append(destino)
                for ady in self.__adyPonderado[destino]:
                    if ady[0] not in visitados:
                        adyacente = (ady[1], destino, ady[0])
                        pq.put(adyacente)
                grafo_resultante.append(arista)
        return grafo_resultante
