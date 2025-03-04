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

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

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

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def print_list(self) -> None:
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)) if elements else "Empty list")

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data