from __future__ import annotations


class Scope:
    """Responsible for giving variables unique names."""

    def __init__(self, scope_name: str, parent: Scope = None):
        self._name = scope_name
        self._parent = parent
        self._variable_names = {}

    _mangle_seperator = '.'

    def _mangling(self):
        if self._parent is None:
            return self._name + self._mangle_seperator

        return self._parent._mangling() + self._name + self._mangle_seperator

    def register(self, name: str):
        """Adds a variable to the scope."""
        if name in self._variable_names:
            raise KeyError(f"Variable '{name}' already exists.")

        self._variable_names[name] = self._mangling() + name

    def get(self, name: str) -> str:
        """Returns a variable's mangled name from the scope or from its parents."""
        if name in self._variable_names:
            return self._variable_names[name]

        if self._parent is None:
            raise KeyError(f"Variable '{name}' does not exist.")

        return self._parent.get(name)

    def get_all(self):
        """Returns the mangled names of all variables in the current scope."""
        yield from self._variable_names.values()
