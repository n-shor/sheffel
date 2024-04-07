from __future__ import annotations

from ..structure import abstract
from ..structure import resolved


class Resolver(resolved.Scope):
    """Resolves operators for function names and variable sub-attributes. Name mangles variables and functions."""

    _types: list[resolved.TypeDeclaration] = []
    _functions: list[resolved.FunctionDeclaration] = []

    def __init__(self, parent: Resolver = None):
        super().__init__(scope_name, parent)



    def translate(self, source: abstract.Node) -> resolved.Node:
        match source:
            case abstract.Block(nodes=nodes):

                translator = Resolver(str(self._get_block_id()), self)

                return resolved.Block(tuple(translator.translate(node) for node in nodes))

            case abstract.Declaration(name=name, type_=type_):
                return

            case abstract.FunctionComposition(return_type=ret_type, arguments=args, body=body):
                self._functions.append(resolved.FunctionDeclaration())

                return 'fpointer'

            case abstract.ArrayComposition():
                pass

            case abstract.MemoryComposition():
                pass

            case abstract.Operator(operation='{}', operands=(abstract.type_type, abstract.Block(nodes=fields))):
                for field in fields:
                    pass

            case abstract.Operator(operation='{}', operands=(type_, abstract.Block(nodes=fields))):
                return resolved.TypeInitialization(type_, fields)
