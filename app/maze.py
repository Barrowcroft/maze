"""
The maze loader module provides the function to load the maze text file
into a Maze object, and provides a function to retieve the neighbours of a given cell,
and the Manhatten value of a given cell.

In the maze definition an asterisk represents a wall,
'A' represents the start position and 'B' represents the goal.

Cooridnates in the maze are given and returned as (row, col).
"""

from __future__ import annotations

import os
from typing import List, Tuple


class Maze:
    """
    Maze

    Defines the Maze class.
    """

    def __init__(self) -> None:
        """
        __init__

        Initialises the maze class.
        """

        self.maze: list[list[str]] = []
        self.start: Tuple[int, int] = (0, 0)  # row, col
        self.goal: Tuple[int, int] = (0, 0)  # row, col
        self.rows: int = 0
        self.cols: int = 0

        self.load()

    def get_start(self) -> Tuple[int, int]:
        """
        get_start

        Return the location of the start cell (row, col).

        Returns:
            Tuple[int, int]: The location of the start cell (row, col).
        """
        return self.start

    def get_goal(self) -> Tuple[int, int]:
        """
        get_goal

        Return the location of the goal cell (row, col).

        Returns:
            Tuple[int, int]: The location of the goal cell (row, col).
        """
        return self.goal

    def get_neighbours(
        self, cell: Tuple[int, int]
    ) -> List[Tuple[str, Tuple[int, int]]]:
        """
        get_neighbours

        Returns a list of the neighbours of a given cell.
        The return incliudes an action "up", "down" etc. and the
        coordinates of the resulting cell if that action is followed.

        Args:
            cell (Tuple[int, int]): The cell to check (row, col).

        Returns:
            List[Tuple[str, Tuple[int, int]]]: The list of neighbours.
        """
        row: int = cell[0]
        col: int = cell[1]
        possible_actions = {
            "N": (row - 1, col),
            "W": (row, col - 1),
            "S": (row + 1, col),
            "E": (row, col + 1),
        }

        neighbours: List[Tuple[str, Tuple[int, int]]] = []
        for action, (_row, _col) in possible_actions.items():
            if (
                0 <= _row < self.rows
                and 0 <= _col < self.cols
                and self.maze[_row][_col] != "*"
            ):
                neighbours.append((action, (_row, _col)))

        return neighbours

    def get_manhattan(self, cell: Tuple[int, int]) -> int:
        """
        get_manhattan

        Returns the Manhattan value from a given cell to the goal cell.

        Args:
            cell (Tuple[int, int]): The cell to check(row, col).
        """
        row: int = cell[0]
        col: int = cell[1]
        if 0 <= col < self.cols and 0 <= row < self.rows:
            return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])

        raise ValueError(
            f"Cell outside maze limits {row,col}. "
            + f"There are {self.rows} rows (0-{self.rows-1}) "
            + f"and {self.cols} cols (0-{self.cols-1})."
        )

    def load(self, filename: str = "maze.txt") -> None:
        """
        loads

        Loads a specified maze file from the 'mazes' directory,
        and count the rows and columns.

        Args:
            filename (str, optional): The maze file to load. Defaults to "maze.txt".
        """
        _directory = "mazes"

        try:

            # Get the directory of the current script

            _current_dir = os.path.dirname(os.path.abspath(__file__))

            # Build the path to the 'smazes' subdirectory

            _directory = os.path.join(_current_dir, _directory)

            # Open the maze file

            with open(os.path.join(_directory, filename), "r", encoding="utf-8") as f:
                _lines = f.readlines()

            # Load the maze into the 2D list.

            self.rows = 0
            for i, _row in enumerate(_lines):
                self.rows += 1
                self.cols = 0
                for j, _col in enumerate(_row):
                    self.cols += 1
                    if _col == "A":
                        self.start = (i, j)
                    if _col == "B":
                        self.goal = (i, j)
                self.maze.append(list(_row))

        except FileNotFoundError as err:
            raise FileNotFoundError(f"Maze '{filename}' not found.") from err
