class RecursiveDescentParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.stack = []
        self.index = 0
        self.input_string = ""
