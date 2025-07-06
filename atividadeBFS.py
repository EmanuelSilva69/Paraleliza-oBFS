import subprocess
import sys

PALINDROMO_SCRIPT = "maquina_palindromo_mt.py"
DIVISIVEL3_SCRIPT = "maquina_divisivel3_mt.py"

def verificar_binario(binario: str) -> bool:
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
        print(f"O número {valor} é palíndromo e divisível por 3 ")
    else:
        print(f"O número {valor} não é palíndromo ou não é divisível por 3 ")