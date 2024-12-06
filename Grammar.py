class Grammar:
    def __init__(self):
        self.nonTerminals = set()
        self.terminals = set()
        self.startSymbol = None
        self.productions = {}

    def read_grammar_from_file(self, filename):
        """Reads a grammar from a file and initializes the sets and productions."""
        with open(filename, 'r') as file:
            lines = file.readlines()

        section = None

        for line in lines:
            line = line.strip()

            if line.startswith("~nonTerminals"):
                section = 'nonTerminals'
                continue
            elif line.startswith("~terminals"):
                section = 'terminals'
                continue
            elif line.startswith("~startSymbol"):
                section = 'startSymbol'
                continue
            elif line.startswith("~productions"):
                section = 'productions'
                continue

            if section == 'nonTerminals':
                self.nonTerminals.update(line.split())
            elif section == 'terminals':
                self.terminals.update(line.split())
            elif section == 'startSymbol':
                self.startSymbol = line
            elif section == 'productions':
                # Handle the productions and store them in a dictionary
                nonTerminal, rules = line.split('–>')  # Split the rule into left and right
                nonTerminal = nonTerminal.strip()
                rules = rules.strip().split('|')  # Handle alternatives in productions
                self.productions[nonTerminal] = [rule.strip() for rule in rules]

    # def load_grammar(self, file_path):
    #     """
    #     :param file_path: Path to the file containing the grammar.
    #     :raises ValueError: If the grammar is not a valid context-free grammar.
    #     """
    #     with open(file_path, 'r') as file:
    #         self.non_terminals = self._parse_line(file.readline())
    #         self.terminals = self._parse_line(file.readline())
    #         self.start_symbol = file.readline().split('=')[1].strip()
    #         file.readline()
    #         prod_rules = [line.strip() for line in file]
    #         self.rules = self._interpret_rules(prod_rules)
    #
    #         if not self._is_valid_cfg(prod_rules):
    #             raise ValueError('The provided grammar is not a valid CFG')

    def nonTerminals_list(self):
        """Returns the list of non-terminal symbols.
        """
        self.nonTerminals

    def terminals_list(self):
        """ Returns the list of terminal symbols.
        """
        self.terminals

    def print_productions(self):
        """Prints all the production rules.
        """
        for nonTerminal, rules in self.productions.items():
            print(f"{nonTerminal} → {' | '.join(rules)}")

    def start_symbol(self):
        """ Returns the start symbol.
        """
        return self.startSymbol

    def productions_for(self,nonTerminal):
        """
        :param non_terminal: Non-terminal symbol to get productions for.
        :return: List of production rules for the given non-terminal.
        """
        return self.productions.get(nonTerminal, [])

    def has_additional_production(self, nonTerminal,production_number):
        """
        Checks if there is an additional production rule for a given non-terminal symbol
        :param non_terminal: Non-terminal symbol to check
        :param production_number: Current production number
        :return: True if there is another production, False otherwise
        """
        return self.productions[nonTerminal][-1][1] != production_number

    def specific_production(self, nonTerminal, production_number):
        """
        :param non_terminal: Non-terminal symbol to get the production for.
        :param production_number: The production number to retrieve.
        :return: Specific production rule if found, None otherwise.
        """
        for production in self.rules[nonTerminal]:
            if production[1] == production_number:
                return production

    def print_productions_for_nonTerminal(self, nonTerminal):
        """Prints the productions for a given non-terminal."""
        if nonTerminal in self.productions:
            print(f"Productions for {nonTerminal}:")
            for rule in self.productions[nonTerminal]:
                print(f"  {nonTerminal} → {rule}")
        else:
            print(f"No productions found for {nonTerminal}")

    def is_CFG(self):
        """Checks if the grammar is a Context-Free Grammar (CFG)."""
        for nonTerminal, rules in self.productions.items():
            # Check if there is exactly one non-terminal on the left-hand side
            if len(nonTerminal.split()) > 1 and nonTerminal.split()[1]!="'":
                print(f"Invalid production: Left-hand side '{nonTerminal}' is not a single non-terminal.")
                return False
        # If no invalid rules are found, return True
        print("The grammar is a valid Context-Free Grammar (CFG).")
        return True

    @staticmethod
    def _parse_line(line):
        """
        :param line: Line from the grammar file.
        :return: List of symbols extracted from the line.
        """
        parts = line.strip().split('=', 1)[1]
        if parts.strip()[-1] == ',':
            parts = [',']
        return [item.strip() for item in parts.split(',')]

    @staticmethod
    def _interpret_rules(rule_lines):
        """
        :param rule_lines: Lines from the grammar file representing the rules.
        :return: Dictionary of interpreted production rules.
        """
        productions = {}
        index = 1

        for rule in rule_lines:
            left_side, right_side = rule.split('->')
            left_side = left_side.strip()
            right_side = [val.strip() for val in right_side.split('|')]

            for production in right_side:
                if left_side in productions:
                    productions[left_side].append((production, index))
                else:
                    productions[left_side] = [(production, index)]
                index += 1
        return productions
