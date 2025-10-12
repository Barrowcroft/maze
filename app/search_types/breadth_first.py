"""
Breadth first search.
"""

from __future__ import annotations

from typing import Tuple

from app.search_pattern import Node, SearchPattern


def load() -> Tuple[str, SearchPattern]:
    """
    load

    Loads the search pattern.
    Registration informaiton includes:
        str, The name of the search pattern.
        Frontier, The search pattern object.

    Returns:
        Tuple[int, str, Frontier]: The registration intormation.
    """
    return ("Breadth First search", BreadthFirst())


class BreadthFirst(SearchPattern):
    """
    BreadthFirst

    The breadth first search pattern.
    """

    def remove_from_frontier(self) -> Node:  # FIFO
        """
        remove_from_frontier

        Removes an item from the frontier buffer to be processed.
        It is this function that distinguishes the search patterns.

        Raises:
            ValueError: To indicate the frontier buffer is empty.

        Returns:
            Node: The removed node.
        """
        if self.empty_frontier():
            raise ValueError("Empty frontier")

        # Remove the first node. FIFO.

        _node: Node = self.frontier_buffer.pop(0)
        return _node
