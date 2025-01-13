"""Implementacion de Cola basado en lista enlazada
"""
from typing import Any

from Estructuras.LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.queue_list = LinkedList()
        self.size = 0

    def enqueue(self, data: Any) -> None:
        """Agrega un elemento a la cola
        """
        self.queue_list.add(data)
        self.size += 1

    def dequeue(self) -> Any:
        """Desencola un elemento
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        data = self.peek()
        self.queue_list.remove_at(0)
        self.size -= 1
        return data

    def peek(self) -> Any:
        """Regresa el elemento proximo a desencolar sin eliminarlo
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue_list.get(0)

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size
