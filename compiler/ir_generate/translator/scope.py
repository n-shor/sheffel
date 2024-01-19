from __future__ import annotations

from llvmlite import ir


class Scope:
    def __init__(self, parent: Scope | None, parameters: dict[str, ir.Argument]):
        self._parent = parent
        self._allocations: dict[str, ir.AllocaInstr] = {}
        self._parameters: dict[str, ir.Argument] = parameters

    def allocate(self, name: str, type_: ir.Type, builder: ir.IRBuilder):
        """Allocates a named variable of the given type on the stack.
        Returns the relevant label to write to."""
        if name in self._allocations:
            raise KeyError(f'"{name}" is already allocated.')

        allocation = builder.alloca(type_)
        self._allocations[name] = allocation
        return allocation

    def read(self, name: str, builder: ir.IRBuilder):
        """Adds an instruction reading the named variable and returns the relevant virtual register to read from."""
        if name in self._allocations:
            return builder.load(self._allocations[name])

        if name in self._parameters:
            return self._parameters[name]

        if self._parent is not None:
            return self._parent.read(name, builder)

        raise KeyError(f'"{name}" is neither allocated nor is a parameter name.')

    def write(self, name: str, builder: ir.IRBuilder):
        """Returns the relevant virtual register for writing to the named variable."""
        if name in self._allocations:
            return self._allocations[name]

        if name in self._parameters:
            raise KeyError(f'"{name}" is a parameter and cannot be written to.')

        if self._parent is not None:
            return self._parent.write(name, builder)

        raise KeyError(f'"{name}" is not allocated.')
