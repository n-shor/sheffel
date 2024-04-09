from __future__ import annotations

from llvmlite import ir

import compiler.structure.resolved.values.literal_value
import compiler.structure.resolved.variables.copy_variable
import compiler.structure.resolved.variables.eval_variable
from ..structure import abstract
from ..structure import resolved


class ModuleAssembler(resolved.Scope):
    """Translates abstract node representation into a llvm ir module."""
    def __init__(self):
        super().__init__(self._get_predefined_scope())
        self.module = ir.Module()

    def translate(self, main: abstract.Node) -> ir.Module:
        main_function_type = ir.FunctionType(ir.IntType(32), ())
        main_function = ir.Function(self.module, main_function_type, 'main')
        assembler = FunctionAssembler(main_function, self)
        assembler.translate(main)
        return self.module

    @staticmethod
    def _get_predefined_scope():
        scope = resolved.Scope(None)
        scope.register("Type", resolved.Type(ir.VoidType(), 'Type'))
        scope.register("Int", resolved.Type(ir.IntType(32), 'Int'))
        scope.register("Double", resolved.Type(ir.DoubleType(), 'Double'))
        return scope


class FunctionAssembler(resolved.Scope):
    """Writes the code for a llvm ir function."""

    def __init__(self, function: ir.Function, parent: resolved.Scope):
        super().__init__(parent)
        self.function = function

    def translate(self, source: abstract.Node):
        block = self.function.append_basic_block('entry')
        assembler = BlockAssembler(ir.IRBuilder(block), self)
        assembler.translate(source)


class BlockAssembler(resolved.Scope):
    """Writes the code for a llvm ir basic block."""

    def __init__(self, builder: ir.IRBuilder, parent: resolved.Scope):
        super().__init__(parent)
        self.builder = builder

    def translate(self, source: abstract.Node):
        match source:
            case abstract.Block(nodes=nodes):
                assembler = BlockAssembler(self.builder, self)
                for node in nodes:
                    try:
                        assembler.translate(node)
                    except resolved.CompilationError:
                        raise resolved.CompilerError(f'{node.syntax()} <---- Here')

            case abstract.IntLiteral(py_value=py_value, ir_value=ir_value):
                return compiler.structure.resolved.values.literal_value.LiteralValue(None, py_value, ir_value)

            case abstract.DoubleLiteral(py_value=py_value, ir_value=ir_value):
                return compiler.structure.resolved.values.literal_value.LiteralValue(None, py_value, ir_value)

            case abstract.BoolLiteral(py_value=py_value, ir_value=ir_value):
                return compiler.structure.resolved.values.literal_value.LiteralValue(None, py_value, ir_value)

            case abstract.CharLiteral(py_value=py_value, ir_value=ir_value):
                return compiler.structure.resolved.values.literal_value.LiteralValue(None, py_value, ir_value)

            case abstract.StrLiteral(py_value=py_value, ir_value=ir_value):
                return compiler.structure.resolved.values.literal_value.LiteralValue(None, py_value, ir_value)

            case abstract.Declaration(type_=abstract.MemoryComposition(type_=type_, memory=memory), name=name):

                resolved_type = self.translate(type_)

                if not isinstance(resolved_type, resolved.Type):
                    raise resolved.CompilationError(f"Cannot declare a variable with {type_.syntax()} translated to {resolved_type}.")

                variable = {
                    abstract.Memory.EVAL: compiler.structure.resolved.variables.eval_variable.EvalVariable,
                    abstract.Memory.COPY: compiler.structure.resolved.variables.copy_variable.CopyVariable,
                    abstract.Memory.REF: NotImplemented
                }[memory](resolved_type, name)

                variable.declare(self.builder)
                self.register(name, variable)
                return variable

            case abstract.Declaration(type_=type_):
                if not isinstance(type_, abstract.MemoryComposition):
                    raise resolved.CompilationError(f"Cannot declare a variable with the non-memory type {type_.syntax()}.")

            case abstract.Variable(name=name):
                return self.get(name)

            case abstract.Operator(operation='=', operands=(left, right)):
                variable = self.translate(left)
                value = self.translate(right)

                if not isinstance(variable, resolved.Variable):
                    raise resolved.CompilationError(f"Cannot set to the non-variable {variable}.")

                if not isinstance(value, resolved.Value):
                    raise resolved.CompilationError(f"Cannot set from the non-value {value}.")

                variable.store(self.builder, value.load(self.builder))

            case abstract.Node():
                raise NotImplementedError()












