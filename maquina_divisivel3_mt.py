import sys

class Divisivel3MT:
    def __init__(self, tape, start_state='q0'):
        self.tape = list(tape)
        self.head = 0
        self.state = start_state
        self.accepted = False
        self.transitions = {
            ('q0', '0'): ('q1', ' ', 'R'),
            ('q0', '1'): ('q4', ' ', 'R'),
            ('q0', ' '): ('q_accept', ' ', 'R'),
            ('q1', '0'): ('q1', '0', 'R'),
            ('q1', '1'): ('q1', '1', 'R'),
            ('q1', ' '): ('q2', ' ', 'L'),
            ('q2', '0'): ('q3', ' ', 'L'),
            ('q2', ' '): ('q0', ' ', 'R'),
            ('q3', '0'): ('q3', '0', 'L'),
            ('q3', '1'): ('q3', '1', 'L'),
            ('q3', ' '): ('q0', ' ', 'R'),
            ('q4', '0'): ('q4', '0', 'R'),
            ('q4', '1'): ('q4', '1', 'R'),
            ('q4', ' '): ('q5', ' ', 'L'),
            ('q5', '1'): ('q6', ' ', 'L'),
            ('q5', ' '): ('q0', ' ', 'R'),
            ('q6', '0'): ('q6', '0', 'L'),
            ('q6', '1'): ('q6', '1', 'L'),
            ('q6', ' '): ('q0', ' ', 'R'),
        }
        self.caminho = []
    def step(self):
        if self.state == 'q_accept':
            self.accepted = True
            return False

        symbol = self.tape[self.head]
        key = (self.state, symbol)
        if key not in self.transitions:
            return False
        self.caminho.append(self.state)
        new_state, new_symbol, move = self.transitions[key]
        self.tape[self.head] = new_symbol
        self.state = new_state
        self.head += 1 if move == 'R' else -1
        return True

    def run(self):
        while not self.accepted:
            if not self.step():
                break
        self.caminho.append(self.state)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(2)
    entrada = sys.argv[1] + ' '
    mt = Divisivel3MT(entrada)
    mt.run()
    print("Estados visitados:", " -> ".join(mt.caminho))  # Novo: imprime o caminho
    sys.exit(0 if mt.accepted else 1)
