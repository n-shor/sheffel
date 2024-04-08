from __future__ import annotations
from abc import ABCMeta


from . import CompilationError


class VariableAlreadyExistsError(CompilationError):
    """Raised when trying to declare a variable with an existing name."""


class VariableMissingError(CompilationError):
    """Raised when trying to access a non-existent variable."""


class Scoped(metaclass=ABCMeta):
    """Represents an object adhering to a scope."""


class Scope:
    """Responsible for storing variables in a stack-like scope structure."""

    def __init__(self, parent: Scope | None):
        self._parent = parent
        self._values = {}

    def register(self, name: str, value: Scoped) -> None:
        if name in self._values:
            raise VariableAlreadyExistsError(f"Variable '{name}' already exists.")

        self._values[name] = value

    def get(self, name: str) -> Scoped:
        if name in self._values:
            return self._values[name]

        if self._parent is None:
            raise VariableMissingError(f"Variable '{name}' does not exist.")

        return self._parent.get(name)
