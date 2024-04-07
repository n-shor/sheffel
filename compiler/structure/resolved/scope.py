from __future__ import annotations


class Scope:
    """Responsible for giving variables a unique id."""

    def __init__(self, parent: Scope = None):
        self._parent = parent
        self._variable_names = {}

    _current_id = 0

    def _get_unique_id(self):
        self._current_id += 1
        return str(self._current_id)

    def register(self, name: str):
        """Adds a variable to the scope."""
        if name in self._variable_names:
            raise KeyError(f"Variable '{name}' already exists.")

        self._variable_names[name] = self._get_unique_id()

    def get(self, name: str) -> str:
        """Returns a variable's id from the scope or from its parents."""
        if name in self._variable_names:
            return self._variable_names[name]

        if self._parent is None:
            raise KeyError(f"Variable '{name}' does not exist.")

        return self._parent.get(name)

    def get_all(self):
        """Returns the mangled names of all variables in the current scope."""
        yield from self._variable_names.values()
