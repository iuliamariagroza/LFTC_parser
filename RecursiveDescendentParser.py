from Moves import Moves


class RecursiveDescentParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.stack = []
        self.index = 0
        self.input_string = ""

    def expand(self,configuration,count):
        configuration.set_move(Moves.EXPAND)

        nonTerminal = configuration.get_input_stack().pop()

        productionRule = self.grammar.get_productions_for_nonTerminal(nonTerminal)[count]

        values = productionRule.split(" ")[::-1]

        workingStack = configuration.get_working_stack()
        workingStack.push(nonTerminal+"-"+(count+1))
        configuration.set_working_stack(workingStack)

        input_stack= configuration.get_input_stack()
        for value in values:
            input_stack.push(value)
        configuration.set_input_stack(input_stack)

        return configuration