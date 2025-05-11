# 5)Eliminar primera instancia
# Nombre de la función: eliminar_primer_instancia(lista, elemento)
# Objetivo: Eliminar la primera ocurrencia de un elemento en la lista y retornarlo.
# Tarea: Buscar la primera aparición de elemento en la lista, eliminarla y retornar el elemento eliminado.
# Si el elemento no existe, retornar None y dejar la lista sin cambios.
# Ejemplo: Si la lista es [5, 3, 5, 7] y se elimina 5, la lista queda [3, 5, 7] y se retorna 5.

def eliminar_primer_instancia(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            eliminado = lista[i]
            for j in range(i, len(lista) - 1):
                lista[j] = lista[j + 1]
            del lista[-1]
            return eliminado
    return None

def eliminar_primer_instancia(lista: list, elemento: int | str | float):
    """
    Elimina la primera ocurrencia de un elemento en la lista y lo retorna.
    Si el elemento no existe, retorna None y deja la lista sin cambios.

    Args:
        lista: La lista en la que se buscará y eliminará el elemento.
        elemento: El elemento a eliminar.

    Returns:
        El elemento eliminado si se encuentra, None en caso contrario.
    """
    indice = -1 
    for i in range(len(lista)):
        if lista[i] == elemento:
            indice = i
            break

    if indice != -1:
        elemento_eliminado = lista[indice] 
        nueva_lista = lista[:indice] + lista[indice + 1:]
        lista[:] = nueva_lista
        return elemento_eliminado
    else:
        return None