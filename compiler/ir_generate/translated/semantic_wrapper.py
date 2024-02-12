from . import Expression


class SemanticWrapper(Expression):
    """Represents an expression which wraps a subexpression and adds no additional instructions to it."""

    def __init__(self, expression: Expression):
        super().__init__(expression.label, expression.type_)


class CopiedExpression(SemanticWrapper):
    """Represents an expression noted by the 'copy' keyword."""


class ViewedExpression(SemanticWrapper):
    """Represents an expression noted by the 'view' keyword."""
