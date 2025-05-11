from manejo_de_listas.agregar_elemento import agregar
from manejo_de_listas.insertar_elemento import insertar
from manejo_de_listas.obtener_indice import obtener_indice
from manejo_de_listas.eliminar_elemento import eliminar
from manejo_de_listas.eliminar_instancia import eliminar_primer_instancia
from manejo_de_listas.eliminar_todas_instancias import eliminar_todos
from manejo_de_listas.vaciar_lista import vaciar_lista

# 1. Agregar un elemento (lista de strings)
nombres = ["Ana", "Luis"]
agregar(nombres, "Carlos")
print("Después de agregar 'Carlos':", nombres)

# 2. Insertar un elemento (lista de mezclas)
elementos = [10, "perro", 3.14]
elementos = insertar(elementos, "gato", 1)
print("Después de insertar 'gato' en el índice 1:", elementos)

# 3. Obtener el índice (lista de letras)
letras = ["a", "b", "c", "b"]
indice = obtener_indice(letras, "b")
print("Índice de la primera ocurrencia de 'b':", indice)

# 4. Eliminar el último elemento (lista de floats)
precios = [10.5, 20.0, 30.25]
ultimo = eliminar(precios)
print("Elemento eliminado (último):", ultimo)
print("Después de eliminar el último elemento:", precios)

# 5. Eliminar la primera instancia (lista de colores)
colores = ["rojo", "verde", "azul", "verde"]
eliminado = eliminar_primer_instancia(colores, "verde")
print("Primera instancia eliminada de 'verde':", eliminado)
print("Después de eliminar la primera instancia de 'verde':", colores)

# 6. Eliminar todas las instancias (lista mixta)
mixta = [1, "hola", 1, "hola", 3]
eliminar_todos(mixta, "hola")
print("Después de eliminar todas las instancias de 'hola':", mixta)

# 7. Vaciar lista (lista de ciudades)
ciudades = ["Buenos Aires", "Córdoba", "Rosario"]
vaciar_lista(ciudades)
print("Después de vaciar la lista de ciudades:", ciudades)
