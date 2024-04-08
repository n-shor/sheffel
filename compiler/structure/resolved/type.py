from llvmlite import ir

from . import Scoped


class Type(Scoped):
    def __init__(self, fields: dict[str, ir.Type], evals: dict[str, ir.Value]):
        self.fields = fields
        self.evals = evals
        self.ir_type = ir.LiteralStructType(tuple(type_ for name, type_ in fields.items()))

    @classmethod
    def primitive(cls, ir_type: ir.Type, evals: dict[str, ir.Value]):
        """Creates a primitive type, which has no "fields" but does have an ir type and eval attributes."""
        instance = cls({}, evals)
        instance.ir_type = ir_type
        return instance

# every "eval" field or function of a type should get inlined while it is still in-scope
