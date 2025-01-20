import sys
# sys.path.append("D:\\MARCOS\\Git\\merlan")

from antlr4 import *
from generated.MERLANErrorListener import MERLANErrorListener
from generated.MERLANLexer import MERLANLexer
from generated.MERLANParser import MERLANParser
from generated.MERLANVisitor import MERLANVisitor
from generated.BESSERGenerator import BESSERGenerator


def merlan_to_besser(input_file, output_file):
    error_listener = MERLANErrorListener()
    input_stream = FileStream(input_file)
    lexer = MERLANLexer(input_stream)
    lexer.removeErrorListeners()  # Remove default error listener
    # lexer.addErrorListener(error_listener)  # We can add it either to the lexer or the parser
    token_stream = CommonTokenStream(lexer)
    parser = MERLANParser(token_stream)

    # Attach custom error listener
    parser.removeErrorListeners()  # Remove default error listener
    parser.addErrorListener(error_listener)

    # Parse the input file
    tree = parser.script()

    # Check for syntax errors
    if error_listener.has_errors():
        print("Errors detected:")
        for error in error_listener.get_errors():
            print(error)
        print("Aborting code generation due to syntax errors.")
        return
    else:
        print('No errors were found!\n')

    # Visit nodes for code generation
    generator = BESSERGenerator()
    python_code = generator.visit(tree)

    # Write to output file
    print(python_code)
    with open(output_file, 'w') as f:
        f.write(python_code)
    print(f"Python code has been written to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python translator.py <input.dsl> <output.py>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    merlan_to_besser(input_file, output_file)
