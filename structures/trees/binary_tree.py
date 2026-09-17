from __future__ import annotations
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """Nodo base para un árbol binario.

    Atributos:
        value (T): El valor o dato contenido en el nodo.
        left (Optional[Node[T]]): Referencia al hijo izquierdo.
        right (Optional[Node[T]]): Referencia al hijo derecho.
    """

    def __init__(
        self,
        value: T,
        left: Optional[Node[T]] = None,
        right: Optional[Node[T]] = None,
    ) -> None:
        self.value: T = value
        self.left: Optional[Node[T]] = left
        self.right: Optional[Node[T]] = right

    @property
    def is_leaf(self) -> bool:
        """Retorna True si el nodo no tiene hijos."""
        return self.left is None and self.right is None

    def __repr__(self) -> str:
        return f"Node({self.value!r})"

    def __str__(self) -> str:
        return str(self.value)
