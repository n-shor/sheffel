from .evaluator import GrammarASTBuilder


def create_ast(code: str):
    """Creates an AST from given code."""
    builder = GrammarASTBuilder()
    return builder.build_ast(code)
