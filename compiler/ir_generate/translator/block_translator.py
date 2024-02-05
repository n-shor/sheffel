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

    def add(self, _expression: Node, *, _write: bool = None, _type_hint: UnqualifiedType = None):
        """Adds a statement to the block."""

        def add(expression: Node, *, write: bool = None, type_hint: UnqualifiedType = None):
            return self.add(expression, _write=_override(write, _write), _type_hint=_override(type_hint, _type_hint))

        match _expression:

            case Literal(value=value, type_=LiteralType() as type_):
                return TranslatedExpression(
                    ir.Constant(resolve_type(type_), value),
                    VariableType(type_, ValueMemoryQualifier(), (ConstBehaviorQualifier(),))
                )

            case Return(returnee=returnee):
                translated = add(returnee)
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
                print('breh')
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
                # with self.builder.if_then(self.add(condition).label) as then_block:

            case Function() as syntax:
                translator = FunctionTranslator(syntax, self.func.module)
                translator.translate()
                return TranslatedExpression(
                    translator.func,
                    syntax.type_
                )

            case VariableDeclaration(name=name, type_=VariableType(base_type=AutoUnqualifiedType() | NamedUnqualifiedType(name='Function')) as type_):
                type_ = VariableType(_type_hint, type_.memory, type_.behavior)
                return self.allocate(name, type_, self.builder)

            case VariableDeclaration(name=name, type_=type_):
                return self.allocate(name, type_, self.builder)

            case Variable(name=name):
                return self.write(name, self.builder) if _write else self.read(name, self.builder)

            # negative literal
            case Operator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType() as type_),)):
                return TranslatedExpression(
                    ir.Constant(resolve_type(type_), -value),
                    VariableType(type_, ValueMemoryQualifier(), (ConstBehaviorQualifier(),))
                )

            case Operator(signature='()', operands=(callee, *parameters)):
                translated_callee = add(callee)

                if not isinstance(translated_callee.type_, FunctionType):
                    raise TypeError(f"Attempted to call a non function: {translated_callee}")

                return TranslatedExpression(
                    self.builder.call(translated_callee.label, (add(param).label for param in parameters)),
                    translated_callee.type_.return_type
                )

            case Operator(signature='=', operands=(assigned, assignee)):
                translated_assignee = add(assignee)
                translated_assigned = add(assigned, write=True, type_hint=translated_assignee.type_.base_type)

                return TranslatedExpression(
                    self.builder.store(translated_assignee.label, translated_assigned.label),
                    translated_assigned.type_
                )

            case Operator(signature='+' | '-' | '*' as signature, operands=(left, right)):
                return TranslatedExpression.type_from_instruction(
                    {
                        '+': self.builder.add,
                        '-': self.builder.sub,
                        '*': self.builder.mul
                    }[signature](add(left).label, add(right).label),
                    ValueMemoryQualifier(),
                    (NoWriteBehaviorQualifier(),)
                )

            case Operator(signature='<' | '<=' | '>' | '>=' | '==' | '!=' as signature, operands=(left, right)):
                return TranslatedExpression.type_from_instruction(
                    self.builder.icmp_signed(signature, add(left).label, add(right).label),
                    ValueMemoryQualifier(),
                    (NoWriteBehaviorQualifier(),)
                )

            case Operator(signature=signature):
                raise ValueError(f'{signature} is an unknown operation.')

            case Node() as node:
                raise TypeError(f'{node} is of a primitive or unknown node type.')

            case other:
                raise TypeError(f'{other} is not a node type.')

    def translate(self) -> bool:
        """Translates the entire block. Returns whether it is successfully terminated."""

        for statement in self.statements:

            match self.add(statement):
                case TranslatedExpression(label=ir.Terminator()):
                    print("Info: stopped translation due to terminator.")
                    return True

        print("Warning: stopped translation without a terminator.")
        return False


def _override(new_arg, old_arg):
    return new_arg if new_arg is not None else old_arg


from .function_translator import FunctionTranslator
