import subprocess
import time
import os
import json
from multiprocessing import Process, Manager
from graphviz import Digraph
import matplotlib.pyplot as plt
import networkx as nx
import imageio
import networkx as nx
import os
PALINDROMO_SCRIPT = "maquina_palindromo_mt.py"
DIVISIVEL3_SCRIPT = "maquina_divisivel3_mt.py"

def animar_caminho(estados, titulo="Animação", output_path="animacao.gif"):
    G = nx.DiGraph()
    for i in range(len(estados) - 1):
        G.add_edge(estados[i], estados[i + 1])

    pos = nx.spring_layout(G, seed=42)
    frames = []

    caminho_total = estados + estados[::-1][1:]  # ida e volta

    for i in range(1, len(caminho_total) + 1):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.clear()

        # desenha todos os nós e arestas
        nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', ax=ax)

        # nós e arestas visitadas até o passo i
        nos_ativos = caminho_total[:i]
        arestas_ativas = [(nos_ativos[j], nos_ativos[j + 1]) for j in range(len(nos_ativos) - 1)]

        nx.draw_networkx_nodes(G, pos, nodelist=nos_ativos, node_color='lightblue', ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=arestas_ativas, edge_color='blue', width=2, ax=ax)

        ax.set_title(f"{titulo} - Passo {i}/{len(caminho_total)}")
        temp_path = f"frame_{i}.png"
        plt.savefig(temp_path)
        frames.append(imageio.v2.imread(temp_path))
        plt.close(fig)
        os.remove(temp_path)

    # Salvar como GIF animado
    imageio.mimsave(output_path, frames, duration=0.5, loop=0)
    return output_path

def extrair_caminho_estados(saida):
    for linha in saida.splitlines():
        if "Estados visitados:" in linha:
            return [estado.strip() for estado in linha.split(":")[1].split("->")]
    return []

def gerar_diagrama_estados_visitados(nome_mt, estados_visitados):
    dot = Digraph(format='png')
    dot.attr(rankdir='LR', size='10,5')

    for i, estado in enumerate(estados_visitados):
        color = 'lightblue' if i < len(estados_visitados) - 1 else 'lightgreen'
        dot.node(estado, shape='circle', style='filled', fillcolor=color)
        if i > 0:
            dot.edge(estados_visitados[i-1], estado)

    output_path = f"{nome_mt}_caminho"
    filename = dot.render(output_path, cleanup=True)
    dot.view()
    return filename



def executar_mt(script, entrada, nome, log):
    inicio = time.time()
    processo = subprocess.run(['python', script, entrada], capture_output=True, text=True)
    fim = time.time()

    status = "ACEITA" if processo.returncode == 0 else "REJEITA"
    saida = processo.stdout.strip()
    caminho = extrair_caminho_estados(saida)
    img_path = gerar_diagrama_estados_visitados(nome, caminho)
    anim_path = animar_caminho(caminho, f"MT {nome}", f"{nome}_animacao.png")

    log[nome] = {
        "tempo": round(fim - inicio, 4),
        "status": status,
        "saida": saida,
        "caminho": caminho,
        "img": img_path,
        "anim": anim_path
    }

def main():
    binario = input("Digite um número binário: ").strip()

    if not all(c in '01' for c in binario):
        print(" Entrada inválida. Use apenas 0 ou 1.")
        return

    entrada_formatada = binario + " "

    with Manager() as manager:
        log_execucao = manager.dict()

        p1 = Process(target=executar_mt, args=(PALINDROMO_SCRIPT, entrada_formatada, "Palindromo", log_execucao))
        p2 = Process(target=executar_mt, args=(DIVISIVEL3_SCRIPT, entrada_formatada, "Div3", log_execucao))

        print("\n Iniciando subprocessos...")
        inicio_total = time.time()
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        fim_total = time.time()

        print("\n Resultado consolidado:")
        log_dict = dict(log_execucao)
        for nome, info in log_dict.items():
            print(f" Máquina: {nome}")
            print(f"   ↳ Tempo: {info['tempo']}s")
            print(f"   ↳ Status: {info['status']}")
            print(f"   ↳ Caminho: {' → '.join(info['caminho'])}")
            time.sleep(1.5)  # Espera antes de mostrar o próximo
            print(f"   ↳ Diagrama: {info['img']}")
            print(f"   ↳ Animação: {info['anim']}\n")
        if all(info["status"] == "ACEITA" for info in log_dict.values()):
            print(f" O número binário '{binario}' foi ACEITO por ambas as máquinas.")
        else:
            print(f" O número binário '{binario}' foi REJEITADO por pelo menos uma máquina.")

        print(f"⏱️ Tempo total: {round(fim_total - inicio_total, 4)} segundos")

        with open("log_execucao_mt.json", "w") as f:
            json.dump(log_dict, f, indent=4)

if __name__ == "__main__":
    main()
