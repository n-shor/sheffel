from abc import ABCMeta, abstractmethod
from typing import Callable

from llvmlite import ir


class StaticFunction(metaclass=ABCMeta):
    def __init__(self, name: str, type_: ir.FunctionType):
        self.name = name
        self.type_ = type_

    def add_to(self, module: ir.Module):
        """Adds the external function to the module."""
        self.add_body(ir.Function(module, self.type_, self.name))

    @abstractmethod
    def add_body(self, func: ir.Function) -> None:
        ...

    def __call__(self, builder: ir.IRBuilder, *args: ir.Value):
        """Calls the external function"""
        return builder.call(builder.module.globals[self.name], tuple(args))


class InternalFunction(StaticFunction):

    def __init__(self, name: str, type_: ir.FunctionType, body: Callable[..., ir.Value]):
        super().__init__(name, type_)
        self._body = body

    def add_body(self, func):
        builder = ir.IRBuilder(func.append_basic_block())
        self._body(builder, *func.args)

    @classmethod
    def create(cls, type_: ir.FunctionType, *, mangling='_'):
        """Decorates a function which takes the builder as a first argument and then the arguments of its function."""

        def decorator(func: Callable[..., ir.Value]):
            return cls(mangling + func.__name__, type_, func)

        return decorator


class ExternalFunction(StaticFunction):
    def add_body(self, func: ir.Function) -> None:
        pass
