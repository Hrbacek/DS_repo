"""Definicion de Nodos para implementar listas enlazadas, colas y pilas
"""

from typing import Any, Optional

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional[Node] = None
