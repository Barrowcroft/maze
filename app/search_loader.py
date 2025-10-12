"""
The search_loader module provides functions to dynamically load search type modules,
and to list the registered functions.
"""

import importlib
import os
from typing import Dict

from app.search_pattern import SearchPattern


class SearchLoader:
    """
    SearchLoader

    The search type loader class.
    """

    def __init__(self) -> None:
        """
        __init__

        Initialises the search type loader.
        """
        self.registered_search_modules: Dict[str, SearchPattern] = {}

    def import_search_modules(self) -> None:
        """
        import_search_modules

        Imports the search modules from the 'search_types' directory.
        """
        _directory = "search_types"

        try:

            # Get the directory of the current script

            _current_dir = os.path.dirname(os.path.abspath(__file__))

            # Build the path to the 'search_types' subdirectory

            _directory = os.path.join(_current_dir, _directory)

            # List all files in the directory

            _file_names = os.listdir(_directory)

            # Filter only Python files (optional)

            _search_modules = [
                f
                for f in _file_names
                if os.path.isfile(os.path.join(_directory, f)) and f.endswith(".py")
            ]
            _search_modules = sorted(_search_modules)

            # Dynamically import modules

            for _module_name in _search_modules:
                full_module_name = (
                    f"app.search_types.{_module_name[:-3]}"  # Remove .py extension
                )
                _module = importlib.import_module(full_module_name)

                # If the module defines a register() function,
                # call it to register the search type.

                if hasattr(_module, "load"):
                    _name, _action = _module.load()
                    self.registered_search_modules[_name] = _action

        except FileNotFoundError:
            print(f"Directory '{_directory}' not found.")

    def list_search_types(self) -> list[str]:
        """
        list_search_types

        Returns a list of the registered search types.

        Returns:
            list[str]: The list of the registered search types.
        """

        return list(self.registered_search_modules.keys())
