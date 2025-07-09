"""
maquina_divisivel3_mt.py

Este módulo implementa uma Máquina de Turing que reconhece cadeias binárias que representam
números divisíveis por 3. A simulação é feita passo a passo com uma fita unidimensional,
conjunto de estados e transições explícitas.

A cadeia binária é passada como argumento via linha de comando. O programa imprime o caminho
de estados percorrido e retorna código 0 se a entrada for aceita ou 1 caso contrário.

Autor: Emanuel Lopes
Data: 2025-07-08
"""

import sys

class Divisivel3MT:
    """
    Simula uma Máquina de Turing que reconhece cadeias binárias divisíveis por 3.

    A máquina aceita a cadeia se, após o processamento completo, atingir o estado 'q_accept'.
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

    entrada = sys.argv[1] + ' '  # Adiciona espaço final como delimitador
    mt = Divisivel3MT(entrada)
    mt.run()
    print("Estados visitados:", " -> ".join(mt.caminho))
    sys.exit(0 if mt.accepted else 1)
