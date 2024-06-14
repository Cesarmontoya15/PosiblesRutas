from NodosG import *
from Grafo import *
from Rutas import *
from collections import deque
def encontrar_todos_los_caminos(grafo, inicio, fin):
    def bfs(grafo, inicio, fin, todos_caminos):
        cola = deque([[(inicio, None, 0)]])
        while cola:
            camino = cola.popleft()
            nodo, _, distancia = camino[-1]
            if nodo == fin:
                todos_caminos.append((camino.copy(), distancia))
            else:
                for vecino, calle, dist in grafo.get_neighbors(nodo):
                    if vecino not in [p[0] for p in camino]:
                        nuevo_camino = camino + [(vecino, calle, distancia + dist)]
                        cola.append(nuevo_camino)

    todos_caminos = []
    bfs(grafo, inicio, fin, todos_caminos)
    return todos_caminos
def ordenamiento(grafo, inicio, fin):
    # (BFS)
    def bfs(grafo, inicio, fin, todos_caminos):
        # Inicializamos la cola con el nodo de inicio
        cola = deque([[(inicio, None, 0)]])
        # Mientras la cola no esté vacía
        while cola:
            # Sacamos el primer camino de la cola
            camino = cola.popleft()
            # Obtenemos el último nodo del camino, ignoramos la calle y obtenemos la distancia
            nodo, _, distancia = camino[-1]
            # Si el nodo es el nodo final (destino)
            if nodo == fin:
                # Si hemos encontrado menos de 100 caminos
                if len(todos_caminos) < 100:
                    # Añadimos el camino a la lista de todos los caminos
                    todos_caminos.append((camino.copy(), distancia))
                else:  # Si hemos encontrado 100 caminos
                    # Encontramos el índice del camino con la mayor distancia
                    indice_max_distancia = max(range(len(todos_caminos)), key=lambda indice: todos_caminos[indice][1])
                    # Si la distancia del camino actual es menor que la del camino con la mayor distancia
                    if distancia < todos_caminos[indice_max_distancia][1]:
                        # Reemplazamos el camino con la mayor distancia por el camino actual
                        todos_caminos[indice_max_distancia] = (camino.copy(), distancia)
            else:  # Si el nodo no es el nodo final (destino)
                # Para cada vecino del nodo
                for vecino, calle, dist in grafo.get_neighbors(nodo):
                    # Si el vecino no está en el camino actual
                    if vecino not in [p[0] for p in camino]:
                        # Creamos un nuevo camino añadiendo el vecino al camino actual
                        nuevo_camino = camino + [(vecino, calle, distancia + dist)]
                        # Añadimos el nuevo camino a la cola
                        cola.append(nuevo_camino)

    todos_caminos = []
    bfs(grafo, inicio, fin, todos_caminos)
    return todos_caminos
def bubble_sort(caminos):
    n = len(caminos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if caminos[j][1] > caminos[j + 1][1]:  # Compara las distancias totales de los caminos
                caminos[j], caminos[j + 1] = caminos[j + 1], caminos[j]  # Intercambia los caminos si el camino actual es mayor que el siguiente
    return caminos


def print_paths(paths, start, end):
    for i, (path, distance) in enumerate(paths, start=1):
        distance_km = distance / 1000  # convert distance from meters to kilometers
        route = ' -> '.join(f"NODO: ({id}), calle: {street}" for id, street, _ in path[1:])  # skip the first node because it has no street
        print(f"\nCamino: {i} [Inicio: Nodo(1): {start} | Destino: Nodo(35): {end}; Ruta: {route}, Distancia total: {distance_km} km]")  # print distance in kilometers


def ordenamiento_Giros(grafo, inicio, fin):
    # Definimos la función de búsqueda en anchura (BFS)
    def bfs(grafo, inicio, fin, todos_caminos):
        # Inicializamos la cola con el nodo de inicio y un cuarto elemento para los giros
        cola = deque([[(inicio, None, 0, 0)]])
        # Mientras la cola no esté vacía
        while cola:
            # Sacamos el primer camino de la cola
            camino = cola.popleft()
            # Obtenemos el último nodo del camino, ignoramos la calle, obtenemos la distancia y los giros
            nodo, _, distancia, giros = camino[-1]
            # Si el nodo es el nodo final
            if nodo == fin:
                # Creamos una tupla con el camino, la distancia y los giros
                camino_y_distancia_giros = (camino.copy(), distancia, giros)
                # Inicializamos el índice para la inserción
                i = 0
                # Mientras el índice sea menor que la longitud de todos los caminos y la distancia del camino en la posición i sea menor que la distancia actual
                while i < len(todos_caminos) and todos_caminos[i][1] < distancia:
                    # Incrementamos el índice
                    i += 1
                # Insertamos el camino en la posición i
                todos_caminos.insert(i, camino_y_distancia_giros)
                # Si la longitud de todos los caminos es mayor que 100
                if len(todos_caminos) > 100:
                    # Eliminamos el último camino
                    todos_caminos.pop()
            else:  # Si el nodo no es el nodo final
                # Para cada vecino del nodo
                for vecino, calle, dist in grafo.get_neighbors(nodo):
                    # Inicializamos los nuevos giros con los giros actuales
                    nuevos_giros = giros
                    # Si el nombre de la calle cambia, incrementamos los giros
                    if camino[-1][1] != calle:
                        nuevos_giros += 1
                    # Si el vecino no está en el camino actual
                    if vecino not in [p[0] for p in camino]:
                        # Creamos un nuevo camino añadiendo el vecino al camino actual e incluimos los giros en el nuevo camino
                        nuevo_camino = camino + [(vecino, calle, distancia + dist, nuevos_giros)]
                        # Añadimos el nuevo camino a la cola
                        cola.append(nuevo_camino)

    todos_caminos = []
    bfs(grafo, inicio, fin, todos_caminos)
    return todos_caminos

def bubble_sort_por_giros(caminos):
    n = len(caminos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if caminos[j][2] > caminos[j + 1][2]:  # Compara la cantidad de giros de los caminos
                caminos[j], caminos[j + 1] = caminos[j + 1], caminos[j]  # Intercambia los caminos si el camino actual tiene más giros que el siguiente
    return caminos

def print_paths2(paths, start, end):
    for i, (path, distance, turns) in enumerate(paths, start=1):  # Unpack turns from each tuple
        distance_km = distance / 1000  # convert distance from meters to kilometers
        route = ' -> '.join(f"NODO: ({id}), calle: {street}" for id, street, _, _ in path[1:])  # skip the first node because it has no street
        print(f"\nCamino: {i} [[Inicio: Nodo(1): {start} | Destino: Nodo(35): {end}; Ruta: {route}, Distancia total: {distance_km} km, Giros totales: {turns}]")  # print distance in kilometers and total turns

opcion = 0
print("Bienvenido a tu mapa, elige una opcion: ")
while (opcion != 4):
    print("1. Ver todas las posibles rutas ")
    print("2. Ver las rutas de menor a mayor distancia")
    print("3. Ver rutas de menor a mayor cantidad de giros  ")
    print("4. Salir")
    opcion = int(input())
    if(opcion == 1):
        caminosdesorden = encontrar_todos_los_caminos(grafo, "1", "35")
        print_paths(caminosdesorden, "MacDonalds", "Pergamino Cafe")
        print(" ")
    elif(opcion ==2):
        caminosdesorden = ordenamiento(grafo, "1", "35")
        caminos_ordenados = bubble_sort(caminosdesorden)
        print_paths(caminos_ordenados, "MacDonalds", "Pergamino Cafe")
        print(" ")
    elif(opcion==3):
        caminos_desordenados = ordenamiento_Giros(grafo, "1", "35")
        caminos_ordenados = bubble_sort_por_giros(caminos_desordenados)
        print_paths2(caminos_ordenados, "MacDonalds", "Pergamino Cafe")
        print(" ")
    elif(opcion == 4):
        print("¡Hasta luego!")
        print(" ")
        break
    else:
        print("Opcion no valida, intente de nuevo")