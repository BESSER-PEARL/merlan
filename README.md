# MERLAN: Multimodal Environment Requirements Language


## Generate the ANTLR code

In order to generate the ANTLR code (parser, lexer, visitor...), run the following script (we already provide the generated files, so this step is not necessary):

```shell
./scripts/generate_antlr.sh
```

This script will generate the following files into the `generated` folder:

- MERLAN.interp
- MERLAN.tokens
- MERLANLexer.interp
- MERLANLexer.py
- MERLANLexer.tokens
- MERLANListener.py (not used, we use a custom visitor instead, in BESSERGenerator.py)
- MERLANParser.py
- MERLANVisitor.py (not used, we use a custom visitor instead, in BESSERGenerator.py)

The parser is in charge of verifying the provided .merlan code is syntactically correct and conforms to the DSL grammar ([MERLAN.g4](grammar/MERLAN.g4))

We use a custom visitor, [BESSERGenerator](generated/BESSERGenerator.py) to generate executable Pyton code from the .merlan code.

## Generate BESSER (Python) code

Run the following script to evaluate a .merlan file and generate BESSER code:

```shell
./scripts/merlan_to_besser.sh
```

(You can modify the input and output file paths)

This script will run the [main.py](src/main.py) file, with the provided arguments.
