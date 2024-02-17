from .expression import BaseExpression


class SemanticWrapper(BaseExpression):
    """Represents an expression which wraps a subexpression and adds no additional instructions to it."""

    def __init__(self, subexpression: BaseExpression):
        super().__init__()
        self.subexpression = subexpression

    def label(self, builder):
        return self.subexpression.label

    @property
    def type_(self):
        return self.subexpression.type_


class CopiedExpression(SemanticWrapper):
    """Represents an expression noted by the 'copy' keyword."""


class ViewedExpression(SemanticWrapper):
    """Represents an expression noted by the 'view' keyword."""
