from Grammar import Grammar
from RecursiveDescendentParser import RecursiveDescentParser


def main():
    grammar = Grammar()

    file_path = 'g1.in'
    grammar.read_grammar_from_file(file_path)
    parser = RecursiveDescentParser(grammar,out_file="out1.txt", in_file="seq.txt")

    while True:
        print("\n--- Grammar Operations Menu ---")
        print("1. Print non-terminals")
        print("2. Print terminals")
        print("3. Print all productions")
        print("4. Print productions for a specific non-terminal")
        print("5. Check if the grammar is a CFG (Context-Free Grammar)")
        print("6. Parser")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("Non-terminals:",grammar.nonTerminals_list())
        elif choice == '2':
            print("Terminals:",grammar.terminals_list())
        elif choice == '3':
            grammar.print_productions()
        elif choice == '4':
            non_terminal = input("Enter the non-terminal (e.g., 'E', 'T'): ")
            grammar.print_productions_for_nonTerminal(non_terminal)
        elif choice == '5':
            print("Is the grammar a CFG?", grammar.is_CFG())
        elif choice == '6':
            parser.parsing_strategy('')
            # if parser.getState() == 'f':
            #     output = PrintParser(parser.getTree())
            #     output.printToFile('tree.txt')

        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()