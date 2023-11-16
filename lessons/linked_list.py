"""Linked list."""

from __future__ import annotations

class Node:

    data: int
    next: Node

    def __init__(self, data: int, next: Node | None):
        """Construct a node."""
        self.data = data
        self.next = next

    def __str__(self) -> Node:
        """Print values of nodes."""
        if self.next is None:
            return str(self.data)
        else:
            return str(self.data) + "->" + str(self.next)
    