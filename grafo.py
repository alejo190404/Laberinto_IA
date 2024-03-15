class Grafo:
    
    def __init__(self, laberinto):
        self.lista_adyacencia = self.laberinto_a_grafo(laberinto)
        self.laberinto = laberinto  # Guardamos el laberinto para calcular la heurística en A*

    def laberinto_a_grafo(self, laberinto):
        grafo = {}
        n = len(laberinto)  # Asumiendo que el laberinto es cuadrado
        for i in range(n):
            for j in range(n):
                if laberinto[i][j] != 1:  # Si no es una pared
                    vecinos = []
                    if i > 0 and laberinto[i-1][j] != 1:
                        vecinos.append((i-1, j))  # Arriba
                    if i < n-1 and laberinto[i+1][j] != 1:
                        vecinos.append((i+1, j))  # Abajo
                    if j > 0 and laberinto[i][j-1] != 1:
                        vecinos.append((i, j-1))  # Izquierda
                    if j < n-1 and laberinto[i][j+1] != 1:
                        vecinos.append((i, j+1))  # Derecha
                    grafo[(i, j)] = vecinos
        return grafo

    def obtener_vecinos(self, v):
        return self.lista_adyacencia.get(v, [])

    def h(self, nodo, nodo_final):
        # Usando la distancia Manhattan como heurística
        return abs(nodo[0] - nodo_final[0]) + abs(nodo[1] - nodo_final[1])

    def primero_profundidad(self, nodo_inicio, nodo_final):
        visitado = set()
        pila = [(nodo_inicio, [nodo_inicio])]

        while pila:
            (vertice, camino) = pila.pop()
            if vertice not in visitado:
                if vertice == nodo_final:
                    return camino
                visitado.add(vertice)
                for vecino in self.obtener_vecinos(vertice):
                    pila.append((vecino, camino + [vecino]))
        return None

    def primero_anchura(self, nodo_inicio, nodo_final):
        visitado = set()
        cola = [(nodo_inicio, [nodo_inicio])]

        while cola:
            (vertice, camino) = cola.pop(0)
            if vertice not in visitado:
                if vertice == nodo_final:
                    return camino
                visitado.add(vertice)
                for vecino in self.obtener_vecinos(vertice):
                    cola.append((vecino, camino + [vecino]))
        return None

    def a_estrella(self, nodo_inicio, nodo_final):
        import heapq
        cola_prioridad = [(self.h(nodo_inicio, nodo_final), 0, nodo_inicio, [nodo_inicio])]
        visitado = set()

        while cola_prioridad:
            (costo_estimado, costo, vertice, camino) = heapq.heappop(cola_prioridad)
            if vertice not in visitado:
                if vertice == nodo_final:
                    return camino
                visitado.add(vertice)
                for vecino in self.obtener_vecinos(vertice):
                    if vecino not in visitado:
                        nuevo_costo = costo + 1  # Consideramos costo uniforme para cada movimiento
                        heapq.heappush(cola_prioridad, (nuevo_costo + self.h(vecino, nodo_final), nuevo_costo, vecino, camino + [vecino]))
        return None