from llvmlite import ir


class Type:
    def __init__(self, fields: dict[str, ir.Type], evals: dict[str, ir.Value]):
        self.fields = fields
        self.evals = evals
        self.ir_type = ir.LiteralStructType(tuple(type_ for name, type_ in fields.items()))

# every "eval" field or function of a type should get inlined while it is still in-scope
