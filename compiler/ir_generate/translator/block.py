from llvmlite import ir

from ...ast.nodes import *
from ...ast.types.literal_type import NumericLiteralType
from ...ast.types.unqualified_type import UnqualifiedType, NamedUnqualifiedType, DirectUnqualifiedType


class Block:
    """A translation unit consisting of many uninterrupted lines."""

    def __init__(self, func: ir.Function):
        self.func = func
        self.block = self.func.append_basic_block()
        self.builder = ir.IRBuilder(self.block)

        self._binary_operators = {
            '+': self.builder.add,
            '-': self.builder.sub,
            '*': self.builder.mul,
        }

        self._stack_variables: dict[str, ir.AllocaInstr] = {}

        self._types: dict[str, ir.Type] = {
            'Int': ir.IntType(32),
            'Float': ir.FloatType()
        }

    def resolve_type(self, type_: UnqualifiedType):
        """Resolves an unqualified ast type into a valid IR type."""
        match type_:
            case NamedUnqualifiedType(name=name):
                return self._types[name]

            case DirectUnqualifiedType(type_=type_):
                return type_

            case UnqualifiedType():
                raise TypeError(f'{type_} is of a primitive or unknown qualified-type type.')

            case _:
                raise TypeError(f'{type_} is not a qualified-type type.')

    def add(self, statement: Node):
        """Adds a statement to the block."""

        match statement:
            case Return(returnee=returnee):
                return self.builder.ret(self.add(returnee))

            case Literal(value=value, type_=LiteralType(type_=type_)):
                return ir.Constant(type_, value)

            # negative literals
            case UnaryOperator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType(type_=type_)), )):
                return ir.Constant(type_, -value)

            # unary + operator is currently useless
            case UnaryOperator(signature='+', operands=(operand,)):
                return self.add(operand)

            case VariableDeclaration(name=name, type_=VariableType(base_type=type_, memory=ValueMemoryQualifier())):
                allocated = self.builder.alloca(self.resolve_type(type_))
                self._stack_variables[name] = allocated
                return allocated

            case WriteVariable(name=name):
                return self._stack_variables[name]

            case ReadVariable(name=name):
                return self.builder.load(self._stack_variables[name])

            case BinaryOperator(signature='=', operands=(assigned, assignee)):
                return self.builder.store(
                    self.add(assignee),
                    self.add(assigned)
                )

            case BinaryOperator(signature=signature, operands=(left, right)) if signature in self._binary_operators:
                return self._binary_operators[signature](self.add(left), self.add(right))

            case Operator(signature=signature):
                raise ValueError(f'{signature} is an unknown operation.')

            case Node():
                raise TypeError(f'{statement} is of a primitive or unknown node type.')

            case _:
                raise TypeError(f'{statement} is not a node type.')

    def translate(self, statements: list[Node]):
        """Adds multiple statements to the block."""

        for statement in statements:
            self.add(statement)

        # print("Warning: missing terminator.")
