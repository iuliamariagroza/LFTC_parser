class Configuration:
    def __init__(self,move,state_of_parsing, position_current_symbol,working_stack, input_stack):
        if working_stack is None:
            working_stack = []
        if input_stack is None:
            input_stack = []
        self.move = move
        self.state_of_parsing = state_of_parsing
        self.position_current_symbol = position_current_symbol
        self.working_stack = working_stack
        self.input_stack = input_stack

    def get_move(self):
        return self.move

    def set_move(self, move):
        self.move = move

    def get_state_of_parsing(self):
        return self.state_of_parsing

    def set_state_of_parsing(self, state_of_parsing):
        self.state_of_parsing = state_of_parsing

    def get_position_current_symbol(self):
        return self.position_current_symbol

    def set_position_current_symbol(self, position_current_symbol):
        self.position_current_symbol = position_current_symbol

    def get_working_stack(self):
        return self.working_stack

    def set_working_stack(self, working_stack):
        self.working_stack = working_stack

    def get_input_stack(self):
        return self.input_stack

    def set_input_stack(self, input_stack):
        self.input_stack = input_stack

    def print_input_stack(self):
        reversed_stack = list(reversed(self.input_stack))
        return "[" + ", ".join(reversed_stack) + "]"

    def __str__(self):
        return (f"Configuration{{"
                f"move = {self.move}, "
                f"state_of_parsing = {self.state_of_parsing}, "
                f"position_current_symbol = {self.position_current_symbol}, "
                f"working_stack = {self.working_stack}, "
                f"input_stack = {self.print_input_stack()}"
                f"}}")