# 7) vaciar_lista(lista)
# Nombre de la función: vaciar_lista(lista)
# Objetivo: Eliminar todos los elementos de la lista, dejándola vacía.
# Tarea: Modificar la lista original, removiendo todos sus elementos.
# No es necesario retornar un valor (solo modificar la lista).
# Ejemplo: Si la lista es [1, 2, 3], al llamar a vaciar_lista(), la lista quedará [].

def vaciar_lista(lista: list):
    """
    Elimina todos los elementos de la lista, dejándola vacía.

    Args:
        lista: La lista que se va a vaciar
    """

    while len(lista) > 0:
        del lista[0]