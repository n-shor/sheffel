class calcVisitor:

    def visit_prog(self, context):
        return self.visit_expr(context.expr())

    def visit_expr(self, context):
        if context.op:
            # Handle binary operations
            op = context.op.getText()
            if op == "*":
                return self.visit_expr(context.expr(0)) * self.visit_expr(context.expr(1))
            elif op == "/":
                return self.visit_expr(context.expr(0)) / self.visit_expr(context.expr(1))
            elif op == "+":
                return self.visit_expr(context.expr(0)) + self.visit_expr(context.expr(1))
            elif op == "-":
                return self.visit_expr(context.expr(0)) - self.visit_expr(context.expr(1))
            else:
                raise ValueError(f"Unknown operator: {op}")
        elif context.paren():
            # Handle parenthesized expressions
            return self.visit_expr(context.paren().expr())
        elif context.INT():
            # Handle integers
            return int(context.INT().getText())
        elif context.FLOAT():
            # Handle floats
            return float(context.FLOAT().getText())
        elif context.STR():
            # Handle strings (modify according to your needs)
            return context.STR().getText()
        else:
            raise ValueError(f"Unrecognized expression: {context}")