"""
"""

from typing import Any
from Estructuras.LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.stack_list = LinkedList()
        self.size = 0

    def push(self, data: Any) -> None:
        """Agregar elemento en el tope de la pila
        """
        self.stack_list.add_at(0, data)
        self.size += 1

    def pop(self) -> Any:
        """Elimina y retorna el elemento del tope de la pila
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        data = self.stack_list.get(0)
        self.stack_list.remove_at(0)
        self.size -= 1
        return data

    def peek(self) -> Any:
        """Retorna el elemento en el tope de la pila sin eliminarlo.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack_list.get(0)

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size
