"""
The search ai module contains the solver class which carries out the maze search,
and returns a solution to the maze.
"""

from __future__ import annotations

from typing import Callable, List, Tuple

from app.maze import Maze
from app.search_pattern import Node, SearchPattern


class Solver:  # pylint: disable=too-few-public-methods
    """
    Solver

    The solver class which searches the maze and returns a solution.
    """

    def __init__(self, search_pattern: SearchPattern, maze: Maze) -> None:
        """
        __init__

        Initialised the solver class.

        Args:
            fronsearch_pattern (SearchPattern): The search pattern to use.
            maze (Maze): The maze to solve
        """
        self.search_pattern: SearchPattern = search_pattern
        self.maze: Maze = maze

        self.num_explored: int = 0

    def solve(
        self,
        show_solution: Callable[
            [List[Tuple[int, int]], str, List[Tuple[int, int]], str, int], None
        ],
    ):
        """
        solve

        Invoke the maze solving algorithm.
        """

        self.search_pattern.frontier_buffer = []
        _explored: List[Tuple[int, int]] = []
        _num_explored: int = 0

        # Setup the start node and add it to the frontiewr.

        _start: Node = Node(state=self.maze.get_start(), parent=None, action="")
        self.search_pattern.add_to_frontier(_start)

        # Do the search.

        while True:

            # If not more nodes to search then there is no solution.

            if self.search_pattern.empty_frontier():
                show_solution([], "", [], "", 0)
                return

            # Get the next node to search. It is this function that
            # destinguishes the different search pattersn.

            _node: Node = (
                self.search_pattern.remove_from_frontier()
            )  # This is search specific.
            _num_explored += 1

            # If the node is the goal, then construct the solution
            # and report back.

            if _node.state == self.maze.get_goal():
                _actions: List[str] = []
                _cells: List[Tuple[int, int]] = []

                while _node.parent is not None:
                    _actions.append(_node.action)
                    _cells.append(_node.state)
                    _node = _node.parent
                _actions.reverse()
                _cells.reverse()

                show_solution(_cells, "#C17E7E", _explored, "#7A9EB1", _num_explored)
                return

            # Add the node to the list of those explored, and report it.

            _explored.append(_node.state)
            show_solution([], "", [_node.state], "#7C9A6D", 0)

            # Add the node's neighbours to the frontier.

            for _action, _state in self.maze.get_neighbours(_node.state):

                if (
                    not self.search_pattern.frontier_contains_state(_state)
                    and _state not in _explored
                ):
                    child = Node(
                        state=_state,
                        parent=_node,
                        action=_action,
                        manhattan=self.maze.get_manhattan(_state),
                        cost=_num_explored,
                    )
                    self.search_pattern.add_to_frontier(child)
