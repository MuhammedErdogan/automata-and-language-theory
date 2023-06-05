

class TuringMachine(object):
    def __init__(self,
                 tape="",
                 blank_symbol="0",
                 initial_state="",
                 final_states=None,
                 transition_function=None):
        self.tape = list(tape)
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        if transition_function == None:
            self.transition_function = {}
        else:
            self.transition_function = transition_function
        if final_states == None:
            self.final_states = set()
        else:
            self.final_states = set(final_states)

    def step(self):
        if self.head_position >= len(self.tape):
            self.tape.append(self.blank_symbol)
        char_under_head = self.tape[self.head_position]
        x = (self.current_state, char_under_head)
        if x in self.transition_function:
            y = self.transition_function[x]
            self.tape[self.head_position] = y[1]
            if y[2] == 'L':
                self.head_position -= 1
            elif y[2] == 'R':
                self.head_position += 1
            self.current_state = y[0]

    def final(self):
        if self.current_state in self.final_states:
            return True
        else:
            return False

    def print_tape(self):
        print(''.join(self.tape))

# Define the transition rules for unary addition
transition_rules = {
    ("init", "1"): ("init", "1", "R"),
    ("init", "0"): ("add", "1", "R"),
    ("add", "1"): ("add", "1", "R"),
    ("add", "0"): ("final", "1", "R")
}

# Initialize the Turing machine
turing_machine = TuringMachine(
    tape = "11101111",
    blank_symbol = "0",
    initial_state = "init",
    final_states = ["final"],
    transition_function = transition_rules
)

# Execute the Turing machine
while not turing_machine.final():
    turing_machine.step()

# Print the result
turing_machine.print_tape()


class TuringMachine(object):
    def __init__(self, tape="", blank_symbol="0", initial_state="", final_states=None, transition_function=None):
        self.tape = list(tape)
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        if transition_function == None:
            self.transition_function = {}
        else:
            self.transition_function = transition_function
        if final_states == None:
            self.final_states = set()
        else:
            self.final_states = set(final_states)

    def step(self):
        if self.head_position >= len(self.tape):
            self.tape.append(self.blank_symbol)
        char_under_head = self.tape[self.head_position]
        x = (self.current_state, char_under_head)
        if x in self.transition_function:
            y = self.transition_function[x]
            self.tape[self.head_position] = y[1]
            if y[2] == 'L':
                self.head_position -= 1
            elif y[2] == 'R':
                self.head_position += 1
            self.current_state = y[0]

    def final(self):
        if self.current_state in self.final_states:
            return True
        else:
            return False

    def print_tape(self):
        print(''.join(self.tape))
