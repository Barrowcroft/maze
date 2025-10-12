"""
A* search.
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
    return ("A* search", AStar())


class AStar(SearchPattern):
    """
    AStar

    The A* search pattern, using the manhattan value.
    """

    def remove_from_frontier(self) -> Node:  # LIFO
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

        # Remove the node that has the lowest sum of the manhattan value
        # and the cost of getting to that node.

        _node = min(self.frontier_buffer, key=lambda node: node.manhattan + node.cost)
        self.frontier_buffer.remove(_node)

        return _node
