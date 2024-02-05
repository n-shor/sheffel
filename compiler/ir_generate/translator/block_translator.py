from ...ast.nodes import *
from ...ast.types import *

from . import resolve_type, TranslatedExpression, Scope


class BlockTranslator(Scope):
    """A translation unit consisting of many uninterrupted lines."""

    def __init__(self, syntax: Block, func: ir.Function, parent: Scope):
        self.statements = syntax.statements
        self.func = func
        self.block = self.func.append_basic_block()
        self.builder = ir.IRBuilder(self.block)

        super().__init__(parent, {})

    def _arithmetic_operator(self, signature: str, left: Node, right: Node):
        """Adds the relevant arithmetic instruction between left and right."""

        translated_left = self.add(left)
        translated_right = self.add(right)

        integer_operations = {
            '+': self.builder.add,
            '-': self.builder.sub,
            '*': self.builder.mul
        }

        floating_operations = {
            '+': self.builder.fadd,
            '-': self.builder.fsub,
            '*': self.builder.fmul
        }

        try:
            instruction = integer_operations[signature](translated_left.label, translated_right.label)

        except TypeError:
            instruction = floating_operations[signature](translated_left.label, translated_right.label)

        return TranslatedExpression.make_from_instruction(instruction)

    def add(self, expression: Node, **kwargs):
        """Adds a statement to the block."""

        match expression:

            case Literal(value=value, type_=LiteralType() as type_):
                return TranslatedExpression(
                    ir.Constant(resolve_type(type_), value),
                    VariableType(type_, ValueMemoryQualifier(), (ConstBehaviorQualifier(),))
                )

            case Return(returnee=returnee):
                translated = self.add(returnee, **kwargs)
                return TranslatedExpression(
                    self.builder.ret(translated.label),
                    translated.type_
                )

            case ReturnVoid():
                return TranslatedExpression(
                    self.builder.ret_void(),
                    VoidType()
                )

            case Block() as syntax:
                translator = BlockTranslator(syntax, self.func, self)
                translator.translate()
                return TranslatedExpression(
                    self.builder.branch(translator.block),
                    VoidType()
                )

            case IfElseConditional(condition=condition, then=then, otherwise=otherwise):
                raise NotImplementedError()

            case IfConditional(condition=condition, then=then):
                raise NotImplementedError()

            case Function() as syntax:
                translator = FunctionTranslator(syntax, self.func.module)
                translator.translate()
                return TranslatedExpression(
                    translator.func,
                    syntax.type_
                )

            case VariableDeclaration(name=name, type_=VariableType(base_type=AutoUnqualifiedType() | NamedUnqualifiedType(name='Function')) as type_):
                type_hint: UnqualifiedType = kwargs['type_hint']
                type_ = VariableType(type_hint, type_.memory, type_.behavior)
                return self.allocate(name, type_, self.builder)

            case VariableDeclaration(name=name, type_=type_):
                return self.allocate(name, type_, self.builder)

            case Variable(name=name):
                return self.write(name, self.builder) if 'write' in kwargs else self.read(name, self.builder)

            # negative literal
            case Operator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType() as type_),)):
                return TranslatedExpression(
                    ir.Constant(resolve_type(type_), -value),
                    VariableType(type_, ValueMemoryQualifier(), (ConstBehaviorQualifier(),))
                )

            case Operator(signature='+' | '-' | '*' as signature, operands=(left, right)):
                return self._arithmetic_operator(signature, left, right)

            case Operator(signature='()', operands=(callee, *parameters)):
                translated_callee = self.add(callee, **kwargs)

                if not isinstance(translated_callee.type_, FunctionType):
                    raise TypeError(f"Attempted to call a non function: {translated_callee}")

                return TranslatedExpression(
                    self.builder.call(translated_callee.label, (self.add(param, **kwargs).label for param in parameters)),
                    translated_callee.type_.return_type
                )

            case Operator(signature='=', operands=(assigned, assignee)):
                translated_assignee = self.add(assignee, **kwargs)
                translated_assigned = self.add(assigned, write=True, type_hint=translated_assignee.type_, **kwargs)

                return TranslatedExpression(
                    self.builder.store(translated_assignee.label, translated_assigned.label),
                    translated_assigned.type_
                )

            case Operator(signature=signature):
                raise ValueError(f'{signature} is an unknown operation.')

            case Node():
                raise TypeError(f'{expression} is of a primitive or unknown node type.')

            case _:
                raise TypeError(f'{expression} is not a node type.')

    def translate(self) -> bool:
        """Translates the entire block. Returns whether it is successfully terminated."""

        for statement in self.statements:

            match self.add(statement):
                case TranslatedExpression(label=ir.Terminator()):
                    print("Info: stopped translation due to terminator.")
                    return True

        print("Warning: stopped translation without a terminator.")
        return False

from .function_translator import FunctionTranslator
