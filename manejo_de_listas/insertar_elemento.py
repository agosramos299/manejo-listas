# 2) Insertar
# Nombre de la función: insertar(lista, elemento, indice)
# Objetivo: Insertar un elemento en una posición específica de la lista.
# Tarea: Modificar la lista original, colocando elemento en la posición indicada por indice.
# Si el índice es mayor al tamaño de la lista, el elemento se agrega al final.
# Ejemplo: Si la lista es [10, 20, 30] y se inserta 5 en el índice 1, la lista resultante será [10, 5, 20, 30].

def insertar(lista: list, elemento: int | str | float, indice: int) -> list:
    """
    Inserta un elemento en una posición específica de la lista.

    Args:
        lista: La lista original.
        elemento: El elemento a insertar.
        indice: La posición donde se insertará el elemento.

    Returns:
        La lista modificada con el elemento insertado.
    """
    tamaño = len(lista)

    if indice >= tamaño:
        nueva_lista = lista + [elemento]
    else:
        nueva_lista = lista[:indice] + [elemento] + lista[indice:]

    return nueva_lista

