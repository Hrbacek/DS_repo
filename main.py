from Estructuras.Graph import Graph
from Estructuras.Queue import Queue

from function_catalog import FUNCTION_CATALOG

# comando agregar tarea
def add_task():
    ... # esta funcion toma un nombre de tarea y la ruta de un archivo con código para ejecutar

# comando agregar dependencia
def add_dependency():
    ... # esta funcion toma el nombre de dos tareas y asigna la dependencia de la tarea de la izq como prerrequisito de la derecha

# comando resolver orden ejecucion
def solve_task_order():
    ... # esta funcion toma el grafo que se ha armado, hace print al grafo y luego muestra el orden en que se ejecutaran las tareas

# comando ejecutar pipeline
def execute_pipeline():
    ... # esta funcion ejecuta el código de cada tarea en el orden que resolvió el algoritmo

# Loop principal
def main():
    ...





if __name__ == "__main__":
    main()