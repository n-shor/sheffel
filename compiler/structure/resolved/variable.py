from __future__ import annotations

from .. import abstract


class Variable(abstract.Value):
    """Used to separate variables from their string name."""

    def __init__(self, type_: abstract.Type, original_name: str):
        super().__init__(type_)
        self.original_name = original_name

    class _SubNode(abstract.Node):
        def __init__(self, variable: Variable):
            self.variable = variable

    class _Declaration(_SubNode):
        pass

    class _Copy(_SubNode):
        pass

    def declaration(self):
        return self._Declaration(self)

    def copy(self):
        return self._Copy(self)
