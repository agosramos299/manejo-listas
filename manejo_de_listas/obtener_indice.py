# 3) Obtener indice
# Nombre de la función: obtener_indice(lista, elemento)
# Objetivo: Encontrar el índice de la primera ocurrencia de un elemento en la lista.
# Tarea: Buscar en la lista el elemento recibido y retornar su posición (índice).
# Si el elemento no existe en la lista, retornar -1.

def obtener_indice(lista: list, elemento: int | str | float) -> int:
    
    """
    Encuentra el índice de la primera ocurrencia de un elemento en la lista.

    Args:
        lista (list): La lista en la que se va a buscar.
        elemento: El elemento cuyo índice se busca.

    Returns:
        int: El índice del elemento si se encuentra, o -1 si no se encuentra.
    """
    
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
