"""Definicion de Nodos para implementar listas enlazadas, colas y pilas
"""
from __future__ import annotations # Para anotar next como tipo Nodo
from typing import Any, Optional

class Node:
    def __init__(self, data: Any, next: Optional[Node]=None) -> None:
        self.data = data
        self.next = next
