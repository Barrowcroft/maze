"""
The search pattyrn module provides the definition of a node
and the frontier class required by the search patterns.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Tuple


class Node:
    """
    Node

    The definition of the search node.
    """

    def __init__(
        self,
        state: Tuple[int, int],  # row, col - position in the maze.
        parent: Optional[Node],
        action: str,
        manhattan: int = 0,
        cost: int = 0,
    ) -> None:
        self.state: Tuple[int, int] = state
        self.parent: Optional[Node] = parent
        self.action: str = action
        self.manhattan: int = manhattan
        self.cost: int = cost


class SearchPattern(ABC):
    """
    SearchPattern

    The protocol for the search pattern.
    """

    def __init__(self) -> None:
        """
        __init__

        Initialises the class.
        """
        self.frontier_buffer: list[Node] = []

    def add_to_frontier(self, node: Node) -> None:
        """
        add_to_frontier

        Adds a node the the list of buffered nodes
        in the frontier that are yet to be explored.

        Args:
            node (Node): The node to add.
        """
        self.frontier_buffer.append(node)

    def frontier_contains_state(self, state: Tuple[int, int]) -> bool:
        """
        frontier_contains_state

        Checks to see if the frontier buffer contains a given state.

        Args:
            state (Tuple[int, int]): state to check.

        Returns:
            bool: Returns true is state present.
        """
        return any(_node.state == state for _node in self.frontier_buffer)

    def empty_frontier(self) -> int:
        """
        empty_frontier

        Checks if the frontier buffer is empty.

        Returns:
            int: Returns true if buffer is empty.
        """
        return len(self.frontier_buffer) == 0

    @abstractmethod
    def remove_from_frontier(self) -> Node:
        """Removes an item from the frontier buffer to be processed.
        It is this function that distinguishes the search patterns."""
