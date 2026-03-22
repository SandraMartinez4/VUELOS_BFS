from arbol import Nodo

def buscar_ruta(conexiones, inicio, destino):
    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(inicio)
    nodos_frontera.append(nodo_inicial)

    while nodos_frontera:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == destino:
            return reconstruir_camino(nodo)

        for vecino in conexiones.get(nodo.get_datos(), []):
            hijo = Nodo(vecino)
            hijo.set_padre(nodo)

            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo)

    return None

def reconstruir_camino(nodo):
    camino = []
    while nodo is not None:
        camino.append(nodo.get_datos())
        nodo = nodo.get_padre()
    return list(reversed(camino))
