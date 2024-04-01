from __future__ import annotations

from .. import abstract


class Scope(abstract.Block):
    """Represents a scope: a sequence of code expressions,
    which registers declarations made inside it, as well as being aware of its parent scope."""

    def __init__(self, block: abstract.Block, parent: Scope = None):
        super().__init__(block.nodes)
        self._parent = parent
        self._variables: dict[str, ...] = {}

    class _CtxManager:
        current: Scope = None

        def __init__(self, block: abstract.Block):
            self.this = Scope(block, parent=self.current)

        def __enter__(self):
            type(self).current = self.this
            return self.this

        def __exit__(self, exc_type, exc_val, exc_tb):
            type(self).current = self.this._parent

    @classmethod
    def enter(cls, block: abstract.Block):
        """Creates a new context managed scope, and handles its parents."""
        return cls._CtxManager(block)

    @classmethod
    def current(cls):
        """Returns the active scope."""
        return cls._CtxManager.current

    def create(self, name: str, value):
        """Adds a variable to the scope."""
        if name in self._variables:
            raise KeyError(f"Variable '{name}' already exists.")

        self._variables[name] = value

    def get(self, name: str):
        """Returns a variable from the scope or from its parents."""
        if name in self._variables:
            return self._variables[name]

        if self._parent is None:
            raise KeyError(f"Variable '{name}' does not exist.")

        return self._parent.get(name)

    def syntax(self):
        return f'({', '.join(f'"{name}"' for name in self._variables.keys())}) {super().syntax()}'
