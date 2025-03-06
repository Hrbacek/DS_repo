"""LinkedList modificada para guarda metadatos de listas de adyacencia facilmente
"""
from Estructuras.LinkedList import LinkedList

class Node:
    def __init__(self, value):
        self.value = value # Nombre del nodo 'A', 'B', etc
        self.neighbors = LinkedList() # Lista de adyacencia del nodo (LinkedList sin metadata adicional)
        self.visited = False # flag para realizar DFS

        self.next = None

class GraphLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def __iter__(self): # Usar la lista como iterable
        current = self.head
        while current:
            yield current
            current = current.next
