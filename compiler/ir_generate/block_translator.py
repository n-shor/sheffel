from compiler.ast.nodes import *
from compiler.ast.types import *

from . import resolve_type, TranslatedExpression, Scope
from . import variable
from .variable import create_variable


class BlockTranslator(Scope):
    """A translation unit consisting of many uninterrupted lines."""

    def __init__(self, builder: ir.IRBuilder, parent: Scope):
        self.builder = builder

        super().__init__(parent, {})

    def add(self, _expression: Node):
        """Adds a statement to the block."""

        match _expression:

            case Literal(value=value, type_=LiteralType() as type_):
                return TranslatedExpression(
                    ir.Constant(resolve_type(type_), value),
                    VariableType(type_, ValueMemoryQualifier(), (ConstBehaviorQualifier(),))
                )

            case Return(returnee=returnee):
                translated = self.add(returnee)
                return TranslatedExpression(
                    self.builder.ret(translated.label),
                    translated.type_
                )

            case ReturnVoid():
                return TranslatedExpression(
                    self.builder.ret_void(),
                    VoidType()
                )

            case Function() as syntax:
                function_translator = FunctionTranslator(syntax, self.builder.module)
                function_translator.translate()
                return TranslatedExpression(
                    function_translator.func,  # the function's pointer
                    syntax.type_
                )

            case Block() as syntax:
                return BlockTranslator(self.builder, self).translate(syntax)

            case IfElseConditional(condition=condition, then=then, otherwise=otherwise) if then.returns():
                with self.builder.if_then(self.add(condition).label):
                    self.add(then)

                return self.add(otherwise)

            case IfElseConditional(condition=condition, then=then, otherwise=otherwise):
                with self.builder.if_else(self.add(condition).label) as (then_block, otherwise_block):
                    with then_block:
                        self.add(then)

                    with otherwise_block:
                        self.add(otherwise)

            case IfConditional(condition=condition, then=then):
                with self.builder.if_then(self.add(condition).label):
                    self.add(then)

            case VariableDeclaration() as node:
                raise TypeError(f"{node} should be dealt with at the = operator.")

            # Reads from a variable
            case Variable(name=name):
                var = self.get_variable(name)
                return TranslatedExpression(var.load(), var.get_type())

            # negative literal
            case Operator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType() as type_),)):
                return TranslatedExpression(
                    ir.Constant(resolve_type(type_), -value),
                    VariableType(type_, ValueMemoryQualifier(), (ConstBehaviorQualifier(),))
                )

            case Operator(signature='=', operands=(VariableDeclaration(name=name) as var_declaration, value)):
                translated_value = self.add(value)

                if isinstance(var_declaration.type_.base_type, AutoUnqualifiedType):
                    var_declaration.type_.base_type = translated_value.type_.base_type

                return self._assign(
                    self.add_variable(name, create_variable(self.builder, var_declaration.type_)),
                    translated_value
                )

            case Operator(signature='=', operands=(VariableDeclaration(name=name) as var_declaration, value)):
                translated_value = self.add(value)

                if isinstance(var_declaration.type_.base_type, AutoUnqualifiedType):
                    var_declaration.type_.base_type = translated_value.type_.base_type

                    if isinstance(value, Function):
                        self.add_variable(name, variable.StackVariable(self.builder, type_))

                self.add(var_declaration)
                return self._assign(self.get_variable(name), translated_value)

            case Operator(signature='=', operands=(Variable(name=name), value)):
                return self._assign(self.get_variable(name), self.add(value))

            case Operator(signature='()', operands=(callee, *parameters)):
                translated_callee = self.add(callee)

                if not isinstance(translated_callee.type_.base_type, FunctionType):
                    raise TypeError(f"Attempted to call a non function: {translated_callee}")

                return TranslatedExpression(
                    self.builder.call(translated_callee.label, (self.add(param).label for param in parameters)),
                    translated_callee.type_.base_type.return_type
                )

            case Operator(signature='+' | '-' | '*' as signature, operands=(left, right)):
                return TranslatedExpression.type_from_instruction(
                    {
                        '+': self.builder.add,
                        '-': self.builder.sub,
                        '*': self.builder.mul
                    }[signature](self.add(left).label, self.add(right).label),
                    ValueMemoryQualifier(),
                    (NoWriteBehaviorQualifier(),)
                )

            case Operator(signature='<' | '<=' | '>' | '>=' | '==' | '!=' as signature, operands=(left, right)):
                return TranslatedExpression.type_from_instruction(
                    self.builder.icmp_signed(signature, self.add(left).label, self.add(right).label),
                    ValueMemoryQualifier(),
                    (NoWriteBehaviorQualifier(),)
                )

            case Operator(signature=signature):
                raise ValueError(f'{signature} is an unknown operation.')

            case Node() as node:
                raise TypeError(f'{node} is of a primitive or unknown node type.')

            case other:
                raise TypeError(f'{other} is not a node type.')

    def translate(self, body: Block) -> TranslatedExpression | None:
        """Translates the entire block. Returns its terminator."""

        try:
            for statement in body.statements:
                match self.add(statement):
                    case TranslatedExpression(label=ir.Terminator()) as expr:
                        return expr
        finally:
            with self.builder.goto_block(self.builder.block):  # positions before terminator
                self.free_scope()

    def _assign(self, var: variable.Variable, value: TranslatedExpression):

        match (var.get_type().memory, value.type_.memory):
            case (ValueMemoryQualifier() | ReferenceMemoryQualifier(), ValueMemoryQualifier()):
                return TranslatedExpression(
                    self.builder.store(value.label, var.as_pointer()),
                    value.type_
                )

        raise TypeError(f"Illegal assignment type - {value.type_.memory} to {var.get_type().memory}.")


from .function_translator import FunctionTranslator
