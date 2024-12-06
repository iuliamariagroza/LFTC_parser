class RecursiveDescentParser:
    def __init__(self, grammar,out_file,in_file):
        """
        working stack: working stack alpha which stores the way the parse is built
        input_stack: input stack beta which is a part of the tree to be built
        state: state of the parsing which can take one of the following values:
          • q = normal state
          • b = back state
          • f = final state - corresponding to success:
          • e = error state – corresponding to insuccess:
        i: position of current symbol in input sequence
       :param grammar: grammar of the language for which we will perform the sequence check
        """
        self.grammar = grammar
        self._working_stack = []
        self._input_stack = [self.grammar.start_symbol()]
        self._state = "q"
        self.index = 0
        self._tree = []
        self._out_file = out_file
        self._sequence = []
        self.read_sequence(in_file)
        file = open(self._out_file, 'w')
        file.write("")
        file.close()

    def read_sequence(self, sequence_file):
        with open(sequence_file) as file:
            if sequence_file == "PIF.out":
                line = file.readline()
                while line:
                    elems_line = line.split("'")
                    self._sequence.append(elems_line[1])
                    line = file.readline()
            else:
                line = file.readline()
                while line:
                    self._sequence.append(line.strip())
                    line = file.readline()
        return

    def getTree(self):
        return self._tree

    def getState(self):
        return self._state

    def setState(self, value):
        self._state = value

    def getIndex(self):
        return self._index

    def setIndex(self, value):
        self._index = value

    def getWorkingStack(self):
        return self._working_stack

    def setWorkingStack(self, stack):
        self._working_stack = stack

    def getInputStack(self):
        return self._input_stack

    def setInputStack(self, stack):
        self._input_stack = stack

    def printCurrentConfiguration(self):
        print('**************')
        print('State: {}\n'.format(self._state))
        print('Index: {}\n'.format(self._index))
        print('Working stack: {}\n'.format(self._working_stack))
        print('Input stack: {}\n'.format(self._input_stack))
        print('**************')

    def printCurrentConfigurationToFile(self):
        with open(self._out_file, 'a') as file:
            file.write("\n--------------\n")
            file.write('State: ' + str(self._state) + " ")
            file.write('Index: ' + str(self._index) + "\n")
            file.write('Working stack: ' + str(self._working_stack) + "\n")
            file.write('Input stack: ' + str(self._input_stack) + "\n")

    def write_in_output_file(self, message, final=False):
        with open(self._out_file, 'a') as file:
            if final:
                file.write("Sequence " + str(message) + " is accepted!\n")
            else:
                file.write(message)

    def parsing_strategy(self,w):
        print("sequence:  ", self._sequence)
        w = self._sequence
        while self._state != "f" and self._state != "e":
            self.printCurrentConfiguration()
            if self._state == "q":
                # if self._index == len(w) and len(self._input_stack) == 0:
                #     self.success()
                if len(self._input_stack) == 0:
                    self.momentaryInsuccess()
                elif self._input_stack[0] in self.grammar.nonTerminals_list():
                    self.expand()
                elif self.index < len(w) and self._input_stack[0] == w[self._index]:
                    self.advance()
                else:
                    self.momentaryInsuccess()
        if self._state == "e":
            print('Error at index {}!'.format(self._index))
        else:
            print('Sequence {} is accepted!'.format(w))
            print(self._working_stack)
            self.write_in_output_file(self._working_stack, True)

    def expand(self):
        """
        1.Pop the non-terminal from the input stack
        2.Add the non-terminal to the working stack
        3.Get the first production rule for the non-terminal
        4.Add the corresponding production rule to the input stack
        :return:
        """
        self.write_in_output_file('expand\n', False)
        nonTerminal = self._input_stack.pop(0)
        productionRule = self.grammar.productions_for(nonTerminal)[0]
        self._working_stack.append((nonTerminal, productionRule[1]))
        production_elems= productionRule[0].split('$')
        self._input_stack = production_elems + self._input_stack

    def advance(self):
        """
        1.Pop the top of the input stack (a terminal)
        2.Add it to the working stack
        3.Increase the index
        :return:
        """
        self.write_in_output_file('advance\n', False)
        nonTerminal= self._input_stack.pop(0)
        self._working_stack.append(nonTerminal)
        self.index += 1

    def momentaryInsuccess(self):
        """
        WHEN: head of input stack is a terminal ≠ current symbol from input
        1.State becomes back.
        :return:
        """
        self.write_in_output_file('momentary insuccess\n', False)
        self._state = "b"


