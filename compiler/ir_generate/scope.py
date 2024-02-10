from __future__ import annotations

from .variable import Variable


class Scope:
    def __init__(self, parent: Scope | None, parameters: dict[str, Variable]):
        self._parent = parent
        self._variables: dict[str, Variable] = parameters

    def add_variable(self, name: str, variable: Variable):
        if name in self._variables:
            raise KeyError(f'"{name}" is already allocated.')

        self._variables[name] = variable

    def get_variable(self, name: str):
        if name in self._variables:
            return self._variables[name]

        if self._parent is None:
            raise KeyError(f'"{name}" is not allocated.')

        return self._parent.get_variable(name)

    def free_scope(self):
        for var in self._variables.values():
            var.free()
