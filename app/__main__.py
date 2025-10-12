"""
The __main__ module is the entry point for the maze searching app.

The GUI is provied by subclassing the SearchGUI class.

Them maze is loaded from a text file into a 2D list of strings.

The search types are dynamically loaded from the search_types directory
so future search_types can be added.
"""

from typing import List, Tuple

from app.maze import Maze
from app.search import Solver
from app.search_gui import SearchGUI
from app.search_loader import SearchLoader

_maze: Maze = Maze()
_search_loader: SearchLoader = SearchLoader()


def show_solution(
    cells: List[Tuple[int, int]],
    colour1: str,
    explored: List[Tuple[int, int]],
    colour2: str,
    num_explored: int,
) -> None:
    """
    show_solution

    A link this function will be sent to the AI
    so that it can invoke the function to shwo the search results.

    Args:
        cells (List[Tuple[int, int]]): The cells that makd eup the solution.
        colour1 (str): The colour to show the solution.
        explored (List[Tuple[int, int]]): The cells explored.
        colour2 (str): The colour to show the cells explored.
        num_explored (int): The number of cells explored.
    """
    if cells == explored == []:
        _gui.message("No solution!")
        return

    for _cell in explored:
        if _cell != _maze.start and _cell != _maze.goal:
            _gui.fill_cell(_cell[0] + 1, _cell[1] + 1, colour2)
    for _cell in cells:
        if _cell != _maze.start and _cell != _maze.goal:
            _gui.fill_cell(_cell[0] + 1, _cell[1] + 1, colour1)

    if num_explored:
        _gui.message(f"Solution found in {num_explored} steps.")

    _gui.canvas.update()


def start_search(search_pattern: str) -> None:
    """
    start_search

    A link to this function is passed to the GUI
    so that it can invoke the search when the search button is pressed.

    Args:
        search_pattern (str): The search pattern to use.
    """

    _solver = Solver(_search_loader.registered_search_modules[search_pattern], _maze)
    _solver.solve(show_solution)


_gui: SearchGUI = SearchGUI(None, start_search)

if __name__ == "__main__":

    # Load the maze.

    _maze: Maze = Maze()
    _maze.load()

    # Dynamically load the search types, get their names.

    _search_loader.import_search_modules()
    _search_types = _search_loader.list_search_types()

    # Start GUI.

    _gui.run(
        _search_types,
        _maze.maze,
    )
