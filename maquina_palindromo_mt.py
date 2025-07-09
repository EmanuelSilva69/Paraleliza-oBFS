"""
maquina_palindromo_mt.py

Este módulo implementa uma Máquina de Turing que reconhece se uma cadeia binária
é um palíndromo, utilizando uma lógica simplificada de marcação e transições.

A cadeia binária é passada como argumento via linha de comando. O programa imprime
o caminho de estados percorridos e retorna código 0 se a cadeia for aceita (palíndromo),
ou 1 caso contrário.

Autor: Emanuel Lopes
Data: 2025-07-08
"""

import sys

class PalindromoMT:
    """
    Simula uma Máquina de Turing que reconhece palíndromos binários.

    A máquina aceita a entrada se atingir o estado 'q_accept' após a leitura da fita.
    """

    def __init__(self, tape: str, start_state: str = 'q0'):
        """
        Inicializa a fita, cabeça de leitura, estado inicial e tabela de transições.

        Args:
            tape (str): Cadeia binária de entrada.
            start_state (str, opcional): Estado inicial da máquina. Default é 'q0'.
        """
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

    def step(self) -> bool:
        """
        Executa um único passo da Máquina de Turing, realizando uma transição
        com base no símbolo atual da fita e no estado atual.

        Returns:
            bool: True se uma transição foi realizada; False se a máquina parou.
        """
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

    def run(self) -> None:
        """
        Executa a máquina até que ela seja aceita ou não haja mais transições válidas.
        """
        while not self.accepted:
            if not self.step():
                break
        self.caminho.append(self.state)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(2)

    entrada = sys.argv[1] + ' '  # Adiciona espaço final como marcador de fim
    mt = PalindromoMT(entrada)
    mt.run()
    print("Estados visitados:", " -> ".join(mt.caminho))
    sys.exit(0 if mt.accepted else 1)
