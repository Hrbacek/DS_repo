from Estructuras.GraphLinkedList import GraphLinkedList, Node
from Estructuras.Stack import Stack

class Graph:
    def __init__(self):
        self.nodes = GraphLinkedList()

    def add_node(self, value):
        if not self.nodes.search(value):
            self.nodes.add(value)

    def add_edge(self, from_value, to_value):
        from_node = self.nodes.search(from_value)
        to_node = self.nodes.search(to_value)

        if from_node and to_node:
            if not from_node.neighbors.search(to_value):
                from_node.neighbors.add(to_node.value)
            return True

        return False

    def topological_sort(self)-> GraphLinkedList: # Ordenamiento topologico para orden de tareas
        result = GraphLinkedList()
        stack = GraphLinkedList()  
        
        for node in self.nodes:
            node.visited = False

        for node in self.nodes: # Visita de todos los nodos
            if not node.visited:
                self._dfs(node, stack)

        while stack.head: # Hacer stack de resultados
            top = stack.head.value
            stack.head = stack.head.next
            result.add(top)

        return result
    
    def reversed_topological_sort(self)-> Stack: # Reverso del orden topologico con una Pila
        topological_sort = self.topological_sort()
        reversed = Stack()

        for item in topological_sort:
            reversed.push(item)

        return reversed

    def _dfs(self, node: Node, stack: GraphLinkedList):
        node.visited = True

        for neighbor in node.neighbors:
            neighbor_node = self.nodes.search(neighbor)
            if neighbor_node and not neighbor_node.visited:
                self._dfs(neighbor_node, stack)

        stack.add(node.value)

    def __repr__(self):
        r = ""
        for node in self.nodes:
            r += f"{node.value} -> "
            for neighbor in node.neighbors:
                r += f"{neighbor}, "
            r += "\n"
        return r
