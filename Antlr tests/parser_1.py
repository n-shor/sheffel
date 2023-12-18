from antlr4 import *
from antlr4.InputStream import InputStream
from CalcLexer import calcLexer
from CalcParser import calcParser

class Parser:

    def __init__(self, input_program_filename: str) -> None:
        """
        don't parse yet - just save the program filename
        """
        self.input_program_filename = input_program_filename

    def run(self):
        """
        generate an Abstract Syntax Tree from
        the input program with antlr
        """
        # initialize the antlr parser
        parser = calcParser(
            CommonTokenStream(
                calcLexer(
                    FileStream(
                        self.input_program_filename
            ))))
        
        # parse away !
        # prog is the toplevel rule
        return parser.expr()