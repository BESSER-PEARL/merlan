from antlr4.error.ErrorListener import ErrorListener


class MERLANErrorListener(ErrorListener):
    def __init__(self):
        super(MERLANErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors
