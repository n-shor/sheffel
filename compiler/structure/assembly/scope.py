from __future__ import annotations
from abc import ABCMeta

from llvmlite import ir


class Scoped(metaclass=ABCMeta):
    """Represents an object adhering to a scope."""


class Scope:
    """Responsible for storing variables in a stack-like scope structure."""

    def __init__(self, parent: Scope | None):
        self._parent = parent
        self._values = {}

    def register(self, name: str, value: Scoped) -> None:
        if name in self._values:
            raise KeyError(f"Variable '{name}' already exists.")

        self._values[name] = value

    def get(self, name: str) -> Scoped:
        if name in self._values:
            return self._values[name]

        if self._parent is None:
            raise KeyError(f"Variable '{name}' does not exist.")

        return self._parent.get(name)
