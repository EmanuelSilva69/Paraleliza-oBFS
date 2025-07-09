"""
atividadeBFS.py

Este módulo verifica se uma string binária é simultaneamente um palíndromo e divisível por 3,
utilizando duas Máquinas de Turing simuladas via scripts externos.

Scripts necessários:
- maquina_palindromo_mt.py: Verifica se a cadeia binária é palíndroma.
- maquina_divisivel3_mt.py: Verifica se a cadeia binária representa um número divisível por 3.

O programa principal solicita uma entrada do usuário, valida o conteúdo binário e exibe o resultado da verificação composta.

Autores: Emanuel Lopes
Data: 2025-07-08
"""

import subprocess
import sys

PALINDROMO_SCRIPT = "maquina_palindromo_mt.py"
DIVISIVEL3_SCRIPT = "maquina_divisivel3_mt.py"

def verificar_binario(binario: str) -> bool:
    """
    Verifica se a string binária fornecida é um palíndromo e também representa um número divisível por 3.

    A verificação é feita executando dois scripts externos (Máquinas de Turing):
    - Um para verificação de palíndromo.
    - Um para verificação de divisibilidade por 3.

    Args:
        binario (str): A cadeia binária a ser verificada.

    Returns:
        bool: True se a cadeia for palíndroma e divisível por 3, False caso contrário.
    """
    entrada = binario.strip() + " "
    try:
        p1 = subprocess.run(['python', PALINDROMO_SCRIPT, entrada], capture_output=True)
        p2 = subprocess.run(['python', DIVISIVEL3_SCRIPT, entrada], capture_output=True)
        return p1.returncode == 0 and p2.returncode == 0
    except Exception as e:
        print("Erro durante a execução das MTs:", e)
        return False

if __name__ == "__main__":
    valor = input("Digite um número binário: ").strip()
    if not all(c in '01' for c in valor):
        print("Entrada inválida. Use apenas dígitos binários (0 e 1).")
    elif verificar_binario(valor):
        print(f"O número {valor} é palíndromo e divisível por 3.")
    else:
        print(f"O número {valor} não é palíndromo ou não é divisível por 3.")