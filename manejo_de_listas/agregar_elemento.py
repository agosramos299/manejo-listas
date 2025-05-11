# 1) Agregar
# Nombre de la función:  agregar(lista, elemento)
# Objetivo: Agregar un elemento al final de la lista.
# Tarea: Modificar la lista original, añadiendo elemento como su último elemento. No es necesario retornar un valor (solo modificar la lista).

def agregar (lista: list, elemento: int | str | float):
    """ 
    Agrega un elemento al final de la lista

    """ 
    lista += [elemento]