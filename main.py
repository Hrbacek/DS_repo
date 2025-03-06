from cmd2 import Cmd

from Estructuras.Graph import Graph
from Estructuras.Stack import Stack
from Estructuras.HashTable import HashTable

from Function_catalog.function_catalog import FUNCTION_CATALOG

# comando agregar tarea
def add_task(task_name: str, tasks_graph: Graph):
    if not FUNCTION_CATALOG.get(task_name):
        print("La tarea no se encuentra implementada en el catalogo de funciones")
        return tasks_graph
    tasks_graph.add_node(task_name)
    print(f"Se agregó la tarea {task_name} al grafo de la sesión")
    return tasks_graph


# comando de agregar dependencia
def add_dependency(task_left: str, task_right: str, tasks_graph: Graph):
    result = tasks_graph.add_edge(task_left, task_right)
    if result:
        print(f"Se agregó la dependencia {task_left}->{task_right}")
        return tasks_graph
    print("No se pudo agregar la depencia al grafo")
    return tasks_graph


# comando para resolver orden de ejecucion
def solve_task_order(tasks_graph: Graph)->Stack:
    tasks = tasks_graph.reversed_topological_sort()
    return tasks

def execute_pipeline(tasks_graph: Graph):
    print("Ejecutando el pipeline de tareas...")
    tasks = solve_task_order(tasks_graph)

    while not tasks.is_empty():
        task_name = tasks.pop().value
        print(f"Iniciando la tarea {task_name}")
        task = FUNCTION_CATALOG.get(task_name)
        task()

    print("Fin del pipeline...")

class DAGShell(Cmd):
    prompt = '(dag-cli) '

    def __init__(self):
        super().__init__()
        self.session_dag = Graph()

    def do_add(self, line):
        "Add a task to the DAG"
        self.session_dag = add_task(line.strip(), self.session_dag)

    def do_dependency(self, line):
        "Specify a dependency between two tasks: dependency <task> <dependency>"
        try:
            task, dependency = line.split()
            self.session_dag = add_dependency(task, dependency, self.session_dag)
        except ValueError:
            print("Invalid input. Use: dependency <task> <dependency>")

    def do_execute(self, line):
        "Execute tasks in topological order"
        execute_pipeline(self.session_dag)

    def do_graph(self, line):
        print(self.session_dag)

    def do_clear(self, line):
        self.session_dag = Graph()

    def do_exit(self, line):
        "Exit the CLI"
        print("Exiting...")
        return True

if __name__ == '__main__':
    DAGShell().cmdloop()
