import networkx as nx
import matplotlib.pyplot as plt


class DFA:
    def __init__(self):
        self.states = input("Enter the states, separated by comma: ").split(',')
        self.alphabet = input("Enter the alphabet, separated by comma: ").split(',')
        self.start_state = input("Enter the start state: ")
        self.accept_states = input("Enter the accept states, separated by comma: ").split(',')
        self.transitions = {}

        print("Now, we will define the transition function.")

        for state in self.states:
            self.transitions[state] = {}
            for letter in self.alphabet:
                next_state = input(f"From state {state} on reading input {letter}, which state to transition to? ")
                self.transitions[state][letter] = next_state

    def draw(self):
        G = nx.DiGraph()
        for state in self.states:
            for letter, next_state in self.transitions[state].items():
                G.add_edge(state, next_state, label=letter)

        pos = nx.spring_layout(G)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
        nx.draw(G, pos, with_labels=True,
                node_color=['green' if state in self.accept_states else 'red' for state in G.nodes()])
        plt.show()

    def accept(self, string):
        current_state = self.start_state
        print(f"Initial state: {current_state}")

        for letter in string:
            print(f"Reading input {letter}")
            if letter not in self.transitions[current_state]:
                print(f"Unrecognized symbol '{letter}', machine stuck at state {current_state}")
                return False

            current_state = self.transitions[current_state][letter]
            print(f"Transition to state {current_state}")

        if current_state in self.accept_states:
            print("Input string accepted.")
            return True
        else:
            print("Input string rejected.")
            return False


if __name__ == "__main__":
    dfa = DFA()
    string = input("Enter the string to test: ")
    dfa.draw()
    dfa.accept(string)
