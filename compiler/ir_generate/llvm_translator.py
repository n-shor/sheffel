from ..ast.nodes import *
from llvmlite import ir

class LLVMTranslator:
    
    def __init__(self):
        self.module = ir.Module()
    
    def translate(self, node: Node):
        
        match node:
            case NumericLiteral(value=value):
                return ir.IntType(32)(value)
            
            case BinaryOperator(signature=signature, left=left, right=right):
                
                left = self.translate(left)
                right = self.translate(right)
                
                return ir.Instruction(
                    left.builder,
                    {'+': 'fadd', '-': 'fsub', '*': 'fmul', '/': 'fdiv'}[signature],
                    left, right)
            
            case _:
                print('Unknown node type')
    
    def generate(self, ast: list[Node]):
        for node in ast:
            self.translate(ast)
    
    def get_ir(self):
        return str(self.module)
