from __future__ import annotations

from llvmlite import ir


class VariableScope:
    def __init__(self, outer: VariableScope | None, parameters: dict[str, ir.Argument]):
        self._outer = outer
        self._allocations: dict[str, ir.AllocaInstr] = {}
        self._parameters: dict[str, ir.Argument] = parameters

    def add_named_allocation(self, name: str, allocation: ir.AllocaInstr):
        if name in self._allocations:
            raise KeyError(f'"{name}" is already allocated.')

        self._allocations[name] = allocation
        return allocation

    def get_named_allocation(self, name: str):
        try:
            return self._allocations[name]

        except KeyError:
            if self._outer is not None:
                return self._outer.get_named_allocation(name)
            else:
                raise KeyError(f'"{name}" is not allocated.')

    def get_named_parameter(self, name: str):
        try:
            return self._parameters[name]

        except KeyError:
            if self._outer is not None:
                return self._outer.get_named_parameter(name)
            else:
                raise KeyError(f'"{name}" is not allocated.')

    def get_any(self, name: str):
        try:
            return self.get_named_allocation(name)
        except KeyError:
            return self.get_named_parameter(name)

    def load_any(self, name: str, builder: ir.IRBuilder):
        try:
            return builder.load(self.get_named_allocation(name))
        except KeyError:
            return self.get_named_parameter(name)
