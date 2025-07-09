"""
bfs_mt_explorador.py

Este módulo realiza uma busca em largura (BFS) sobre todas as combinações binárias de tamanho
1 até uma profundidade máxima especificada. O objetivo é identificar quais dessas combinações
são simultaneamente palíndromos e representam números divisíveis por 3, utilizando Máquinas
de Turing simuladas por scripts externos.

Scripts requeridos:
- maquina_palindromo_mt.py: Verifica se a cadeia é palíndroma.
- maquina_divisivel3_mt.py: Verifica se a cadeia é divisível por 3.

O processamento é paralelizado utilizando todos os núcleos da CPU disponíveis.

Autor: Emanuel Lopes
Data: 2025-07-08
"""

import subprocess
from itertools import product
from multiprocessing import Pool, cpu_count

PALINDROMO_SCRIPT = "maquina_palindromo_mt.py"
DIVISIVEL3_SCRIPT = "maquina_divisivel3_mt.py"

def verifica_mt_combinada(entrada: str) -> str | None:
    """
    Verifica se uma string binária é aceita por ambas as Máquinas de Turing:
    uma que testa se a string é um palíndromo e outra que testa se é divisível por 3.

    Args:
        entrada (str): A cadeia binária a ser verificada.

    Returns:
        str | None: A entrada se for aceita por ambas as MTs; caso contrário, retorna None.
    """
    entrada_formatada = entrada + " "
    try:
        p1 = subprocess.run(['python', PALINDROMO_SCRIPT, entrada_formatada], capture_output=True)
        p2 = subprocess.run(['python', DIVISIVEL3_SCRIPT, entrada_formatada], capture_output=True)
        if p1.returncode == 0 and p2.returncode == 0:
            return entrada
    except Exception:
        pass
    return None

def bfs_mt_explorador(profundidade_max: int = 6) -> list[str]:
    """
    Gera todas as combinações de strings binárias de 1 até profundidade_max bits
    e verifica, de forma paralela, quais delas são aceitas por ambas as MTs.

    Args:
        profundidade_max (int): Comprimento máximo das cadeias a serem testadas.
            O valor padrão é 6.

    Returns:
        list[str]: Lista das cadeias aceitas pelas duas Máquinas de Turing.
    """
    entradas = [''.join(bits) for i in range(1, profundidade_max + 1)
                for bits in product('01', repeat=i)]

    with Pool(processes=cpu_count()) as pool:
        resultados = pool.map(verifica_mt_combinada, entradas)

    return [r for r in resultados if r is not None]

if __name__ == "__main__":
    profundidade = 6
    resultados = bfs_mt_explorador(profundidade)
    print(f"Strings binárias de até {profundidade} bits que são palíndromos e divisíveis por 3:")
    for r in resultados:
        print("  -", r)
