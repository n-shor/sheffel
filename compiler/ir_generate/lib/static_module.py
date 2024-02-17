from __future__ import annotations

from typing import Callable

from llvmlite import ir


class StaticModule:
    def __init__(self, name: str):
        self.name = name
        self.functions: list[StaticFunction] = []

    def add_to(self, module: ir.Module):
        for function in self.functions:
            ir.Function(module, function.type_, function.name)


class StaticFunction[T: StaticModule]:
    def __init__(self, parent: T, type_: ir.FunctionType):
        self.type_ = type_
        self.parent = parent
        self.name: str = None

    def set_name(self, name: str, mangle: bool):
        self.name = f'{self.parent.name}.{name}' if mangle else name
        return self.name

    def __call__(self, builder: ir.IRBuilder, *args: ir.Value):
        """Calls the function."""
        if self.name is None:
            raise AssertionError("Function called before being declared or defined.")

        return builder.call(builder.module.globals[self.name], tuple(args))


class ExternalModule(StaticModule):
    """A module of external functions, which does not require generating a file."""

    def __init__(self, name: str):
        super().__init__(name)

    def function(self, type_: ir.FunctionType):
        return ExternalFunction(self, type_)


class ExternalFunction(StaticFunction[ExternalModule]):

    def declare(self, name: str):
        self.name = self.set_name(name, False)
        self.parent.functions.append(self)
        return self


class InternalModule(StaticModule):
    """A module of internal functions, which are kept in a separate file."""

    def __init__(self, name: str):
        super().__init__(name)
        self.module = ir.Module(name)

    def function(self, type_: ir.FunctionType):
        return InternalFunction(self, type_)


class InternalFunction(StaticFunction[InternalModule]):

    def define(self, body: Callable[..., ir.Value]):
        self.name = self.set_name(body.__name__, True)

        func = ir.Function(self.parent.module, self.type_, self.name)
        builder = ir.IRBuilder(func.append_basic_block())
        body(builder, *func.args)

        self.parent.functions.append(self)
        return self
