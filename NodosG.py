class Nodo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


    def __str__(self):
        return f'[ Esquina: {self.nombre} ]'

class Arista:
    def __init__(self, nodo_inicio, nodo_destino, distancia, calle):
        self.nodo_inicio = nodo_inicio
        self.nodo_destino = nodo_destino
        self.distancia = distancia
        self.calle = calle  # store the street name

    def __str__(self):
        return f'RECORRIDO : [{self.nodo_inicio} --> {self.nodo_destino}| Km:{self.peso}]'


