from compiler.ast.nodes import *
from compiler.ast.types import *

from .lib import libc, utils

from . import resolve_type, Scope
from .translated import Expression, TerminatorExpression, CopiedExpression, ViewedExpression, Variable as IRVariable, HeapVariable, StackVariable


class BlockTranslator(Scope):
    """A translation unit consisting of many uninterrupted lines."""

    def __init__(self, builder: ir.IRBuilder, parent: Scope):
        self.builder = builder

        super().__init__(parent, {})

    def add(self, _expression: Node):
        """Adds a statement to the block."""

        match _expression:

            case Literal(value=value, type_=StringLiteralType()):
                return Expression.from_base_type_of(
                    utils.string_literal(self.builder, value),
                    ValueMemoryQualifier(), (NoWriteBehaviorQualifier(), )
                )

            case Literal(value=value, type_=type_):
                return Expression.from_base_type_of(
                    ir.Constant(resolve_type(type_), value),
                    ValueMemoryQualifier(), (NoWriteBehaviorQualifier(), )
                )

            # negative literal
            case Operator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType() as type_), )):
                return Expression.from_base_type_of(
                    ir.Constant(resolve_type(type_), -value),
                    ValueMemoryQualifier(), (NoWriteBehaviorQualifier(), )
                )

            case Return(returnee=returnee):
                translated = self.add(returnee)
                return TerminatorExpression(
                    self.builder.ret(translated.label(self.builder)),
                    translated.type_
                )

            case ReturnVoid():
                return TerminatorExpression(
                    self.builder.ret_void(),
                    VoidType()
                )

            case Copy(copied=copied):
                return CopiedExpression(self.add(copied))

            case View(viewed=viewed):
                return ViewedExpression(self.add(viewed))

            case ExternalCall(external_name=name, parameters=parameters):
                return Expression.from_base_type_of(
                    self._resolve_external(name)(
                        self.builder,
                        *(self.add(param).label(self.builder) for param in parameters)
                    ),
                    ValueMemoryQualifier(), (NoWriteBehaviorQualifier(), )
                )

            case Function() as syntax:
                function_translator = FunctionTranslator(syntax, self.builder.module)
                function_translator.translate()
                return Expression(
                    function_translator.func,  # the function's pointer
                    syntax.type_
                )

            case Block() as syntax:
                return BlockTranslator(self.builder, self).translate(syntax)

            case IfElseConditional(condition=condition, then=then, otherwise=otherwise) if then.returns():
                with self.builder.if_then(self.add(condition).label(self.builder)):
                    self.add(then)

                return self.add(otherwise)

            case IfElseConditional(condition=condition, then=then, otherwise=otherwise):
                with self.builder.if_else(self.add(condition).label(self.builder)) as (then_block, otherwise_block):
                    with then_block:
                        self.add(then)

                    with otherwise_block:
                        self.add(otherwise)

            case IfConditional(condition=condition, then=then):
                with self.builder.if_then(self.add(condition).label(self.builder)):
                    self.add(then)

            case While(condition=condition, body=body):
                preloop_block = self.builder.append_basic_block()
                self.builder.branch(preloop_block)

                self.builder.position_at_start(preloop_block)
                with self.builder.if_then(self.add(condition).label(self.builder)):
                    self.add(body)
                    self.builder.branch(preloop_block)

            case VariableDeclaration(name=name, type_=type_):
                return self.add_variable(name, IRVariable.create(self.builder, type_))

            # Reads from a variable
            case Variable(name=name):
                return self.get_variable(name)

            case Operator(signature='=', operands=(VariableDeclaration(name=name) as var_declaration, value)):
                translated_value = self.add(value)

                if isinstance(var_declaration.type_.base_type, AutoUnqualifiedType):
                    var_declaration.type_.base_type = translated_value.type_.base_type

                return self._assign(
                    self.add_variable(name, IRVariable.create(self.builder, var_declaration.type_)),
                    translated_value
                )

            case Operator(signature='=', operands=(target, value)):
                return self._assign(self.add(target), self.add(value))

            case Operator(signature='()', operands=(callee, *parameters)):
                translated_callee = self.add(callee)

                if not isinstance(translated_callee.type_.base_type, FunctionType):
                    raise TypeError(f"Attempted to call a non function: {translated_callee}")

                return Expression(
                    self.builder.call(
                        translated_callee.label(self.builder),
                        (self.add(param).label(self.builder) for param in parameters)
                    ),
                    translated_callee.type_.base_type.return_type
                )

            case Operator(signature='+' | '-' | '*' | '%' as signature, operands=(left, right)):
                return Expression.from_base_type_of(
                    {
                        '+': self.builder.add,
                        '-': self.builder.sub,
                        '*': self.builder.mul,
                        '%': self.builder.srem
                    }[signature](self.add(left).label(self.builder), self.add(right).label(self.builder)),
                    ValueMemoryQualifier(),
                    (NoWriteBehaviorQualifier(),)
                )

            case Operator(signature='<' | '<=' | '>' | '>=' | '==' | '!=' as signature, operands=(left, right)):
                return Expression.from_base_type_of(
                    self.builder.icmp_signed(signature,
                                             self.add(left).label(self.builder),
                                             self.add(right).label(self.builder)
                                             ),
                    ValueMemoryQualifier(),
                    (NoWriteBehaviorQualifier(),)
                )

            case Operator(signature=signature):
                raise ValueError(f'{signature} is an unknown operation.')

            case Node() as node:
                raise TypeError(f'{node} is of a primitive or unknown node type.')

            case other:
                raise TypeError(f'{other} is not a node type.')

    def translate(self, body: Block) -> TerminatorExpression | None:
        """Translates the entire block. Returns its terminator."""

        try:
            for statement in body.statements:
                match self.add(statement):
                    case TerminatorExpression() as expr:
                        return expr
        finally:
            with self.builder.goto_block(self.builder.block):  # positions before terminator
                for var in self.get_all():
                    var.free(self.builder)

    def _assign(self, var: IRVariable, val: Expression):

        match val:
            case CopiedExpression():
                return Expression(var.assign(self.builder, val.label(self.builder)), val.type_)

            case ViewedExpression(subexpression=val):
                if isinstance(var, HeapVariable) and isinstance(val, HeapVariable):
                    return Expression(var.assign_view(self.builder, val), val.type_)

                raise TypeError(f"View assignment must be between two reference variables, but {var} from {val} given.")

        match (var, val.type_.memory):
            case (HeapVariable(), ReferenceMemoryQualifier()):
                raise TypeError(f"Illegal assignment of a reference to a reference: {var} from {val}.")

            case _:
                return Expression(var.assign(self.builder, val.label(self.builder)), val.type_)

    def _resolve_external(self, name: str):

        match name:
            case 'printf':
                return libc.printf

            case _:
                raise KeyError(f'Unresolved external {name}.')


from .function_translator import FunctionTranslator
