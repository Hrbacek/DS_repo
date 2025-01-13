"""Lista enlazada simple
"""
from typing import Optional, Any
from Estructuras.Node import Node

class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def clear(self):
        """Borra el contenido de la lista enlazada
        """
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, value: Any):
        """Agrega un nodo con el valor al final de la lista
        """
        self.add_at(self.size, value)

    def add_at(self, index: int, value: Any):
        """Agrega un nodo con el valor en el indice
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            new_node = Node(value, self.head)
            self.head = new_node

            if self.is_empty():
                self.tail = new_node

        elif index == self.size:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

        else:
            prev_node = self._get_node(index - 1)
            new_node = Node(value, prev_node.next)
            prev_node.next = new_node

        self.size += 1

    def get(self, index: int)->Any:
        """Obtiene el valor en el nodo del indice
        """
        return self._get_node(index).data

    def set(self, index: int, value: Any):
        """Cambia el valor guardado en el nodo del indice
        """
        node = self._get_node(index)
        node.data = value

    def remove_at(self, index: int):
        """Quita el nodo del indice
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev_node = self._get_node(index - 1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next
            if index == self.size - 1:
                self.tail = prev_node

        self.size -= 1

    def _get_node(self, index: int)->Optional[Node]:
        """Regresa el nodo en el indice
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __len__(self) -> int:
        return self.size