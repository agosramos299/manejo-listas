# 6) Eliminar todas las instancias
# Nombre de la función: eliminar_todos(lista, elemento)
# Objetivo: Eliminar todas las ocurrencias de un elemento en la lista.
# Tarea: Modificar la lista original, removiendo todos los elementos iguales al valor recibido.
# No es necesario retornar un valor (solo modificar la lista).
# Ejemplo: Si la lista es [4, 8, 4, 4, 10] y se eliminan todas las instancias de 4, la lista resultante será [8, 10].

def eliminar_todos(lista: list, elemento: int | str | float):
    """
    Elimina todas las ocurrencias de un elemento en una lista (modificando la lista original).

    Args:
        lista: La lista de la cual se eliminarán los elementos.
        elemento: El elemento que se eliminará de la lista.
    """
    i = 0
    while i < len(lista):
        if lista[i] == elemento:
            for desplazamiento in range(i, len(lista) - 1):
                lista[desplazamiento] = lista[desplazamiento + 1]
            lista[:] = lista[:-1]
        else:
            i += 1

