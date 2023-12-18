#########################
#                       #
# general include files #
#                       #
#########################
from argparse import ArgumentParser

#########################
#                       #
# project include files #
#                       #
#########################
from compiler import Compiler

parser = ArgumentParser()

# input
parser.add_argument(
    "input",
    metavar="<source-code-filename>",
    help="program in our amazing language",
)

# output
parser.add_argument(
    "output",
    metavar="<output-mips-filename>",
    help="to be executed with spim simulator",
)

# optional generation of graphviz dot
# representation of the AST. the dot
# file can then be rendered to a *.png
# image file
parser.add_argument(
    "--dump_ast",
    metavar="<ast-filename>.png",
    help="graphviz dot representation of the AST",
)

# parse the command line arguments
args = parser.parse_args()

# initialize the compiler class
compiler = Compiler(
    input_program_filename = args.input,
    output_mips_filename = args.output,
    ast_png_image_filename = args.dump_ast
)
    
# compile away !
compiler.run()