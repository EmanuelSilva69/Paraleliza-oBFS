import subprocess
from itertools import product
from multiprocessing import Pool, cpu_count

PALINDROMO_SCRIPT = "maquina_palindromo_mt.py"
DIVISIVEL3_SCRIPT = "maquina_divisivel3_mt.py"

def verifica_mt_combinada(entrada: str) -> str | None:
    """
    Verifica se uma string binária é palíndromo E divisível por 3
    utilizando as máquinas de Turing implementadas como scripts.
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

def bfs_mt_explorador(profundidade_max=6):
    """
    Realiza busca BFS sobre todas as combinações binárias de 1 a N bits,
    testando em paralelo se cada uma é aceita pelas duas MTs combinadas.
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
