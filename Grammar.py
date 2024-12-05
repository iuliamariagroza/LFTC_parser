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

    def print_nonTerminals(self):
        """Prints the set of non-terminals."""
        print("Non-terminals:", self.nonTerminals)

    def print_terminals(self):
        """Prints the set of terminals."""
        print("Terminals:", self.terminals)

    def print_productions(self):
        """Prints the set of productions."""
        for nonTerminal, rules in self.productions.items():
            print(f"{nonTerminal} → {' | '.join(rules)}")

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

