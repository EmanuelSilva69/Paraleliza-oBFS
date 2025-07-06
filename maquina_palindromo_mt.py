import sys

class PalindromoMT:
    def __init__(self, tape, start_state='q0'):
        self.tape = list(tape)
        self.head = 0
        self.state = start_state
        self.accepted = False
        self.transitions = {
            ('q0', '0'): ('q0', '0', 'R'),
            ('q0', '1'): ('q1', '1', 'R'),
            ('q0', ' '): ('q_accept', ' ', 'R'),
            ('q1', '0'): ('q2', '0', 'R'),
            ('q1', '1'): ('q0', '1', 'R'),
            ('q2', '0'): ('q1', '0', 'R'),
            ('q2', '1'): ('q2', '1', 'R'),
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
        self.caminho.append(self.state)  # Novo
        new_state, new_symbol, move = self.transitions[key]
        self.tape[self.head] = new_symbol
        self.state = new_state
        self.head += 1 if move == 'R' else -1
        return True

    def run(self):
        while not self.accepted:
            if not self.step():
                break
        self.caminho.append(self.state)  # Adiciona o estado final ao caminho
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(2)
    entrada = sys.argv[1] + ' '
    mt = PalindromoMT(entrada)
    mt.run()
    print("Estados visitados:", " -> ".join(mt.caminho))  # Novo
    sys.exit(0 if mt.accepted else 1)
