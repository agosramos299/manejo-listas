# 4) Eliminar el último elemento
# Nombre de la función: eliminar(lista)
# Objetivo: Eliminar el último elemento de la lista y retornarlo.
# Tarea: Modificar la lista original, removiendo su último elemento.
# Retornar el elemento eliminado.
# Ejemplo: Si la lista es ["a", "b", "c"], al llamar a eliminar(), se retorna "c" y la lista queda ["a", "b"].

def eliminar(lista: list) -> int:
    """
    Elimina el último elemento de la lista y retorna el nuevo estado de la lista

    Args:
        lista: Lista original de la que se eliminará el último elemento.

    Returns:
        int: El elemento eliminado.
    """
    if len(lista) == 0:
        return None
    ultimo = lista[len(lista) - 1]
    del lista[len(lista) - 1]
    return ultimo