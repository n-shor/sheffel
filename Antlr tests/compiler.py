###################
#                 #
# general imports #
#                 #
###################
from typing import Optional

###################
#                 #
# general imports #
#                 #
###################
import subprocess

###################
#                 #
# project imports #
#                 #
###################
from parser_1 import Parser
from ast_pretty_printer import ASTPrettyPrinter

class Compiler:

    def __init__(
        self,
        *, # force keyword arguments
        input_program_filename: str,
        output_mips_filename: str,
        ast_png_image_filename: Optional[str]
    ) -> None:
        """
        API entry point for the compilation process
        """
        self.input_program_filename = input_program_filename
        self.output_mips_filename = output_mips_filename
        
        # generating visualiztion of the AST is optional
        self.visualize_ast = ast_png_image_filename is not None
        self.ast_png_image_filename = ast_png_image_filename

        # allocate an antlr based parser
        self.parser = Parser(input_program_filename)

    def run(self) -> None:

        # step 1:
        # lexical + syntax analysis with antlr
        AST = self.parser.run()
        
        # step 2:
        # generate graphviz dot representation
        visitor = ASTPrettyPrinter()
        ast_graphviz_dot_str = visitor.visit(AST)

        # step 3:
        # render a *.png file from the ast dot file
        # skip generation if user does not want it
        if self.visualize_ast:
            self.generate_png_image_file_of_ast(
                ast_graphviz_dot_str,
                self.ast_png_image_filename
            )

    @staticmethod
    def generate_png_image_file_of_ast(
        ast_graphviz_dot_str: str,
        ast_png_image_filename: str
    ) -> None:

        # graphviz dot header + footer:
        header = "digraph {"
        footer = "}"

        # store the graphviz dot str in a file
        ast_graphviz_dot_filename = (
            ast_png_image_filename +
            ".tmp.dot"
        )
        with open(ast_graphviz_dot_filename, "w") as fl:
            fl.write(
                header +
                ast_graphviz_dot_str +
                footer
            )

        # use dot to render png file
        # from dot specification
        subprocess.run([
            "dot",
            "-Tpng",
            ast_graphviz_dot_filename,
            "-o",
            ast_png_image_filename
        ])