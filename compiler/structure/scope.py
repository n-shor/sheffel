from __future__ import annotations


class Scope[T]:
    def __init__(self, parent: Scope = None):
        self._parent = parent
        self._variables = {}

    def create(self, name: str, value: T):
        """Adds a variable to the scope."""
        if name in self._variables:
            raise KeyError(f"Variable '{name}' already exists.")

        self._variables[name] = value

    def get(self, name: str) -> T:
        """Returns a variable from the scope or from its parents."""
        if name in self._variables:
            return self._variables[name]

        if self._parent is None:
            raise KeyError(f"Variable '{name}' does not exist.")

        return self._parent.get(name)
