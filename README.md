# 🧠 Visualizador de Máquinas de Turing — Palíndromo e Divisibilidade por 3

Este projeto simula e visualiza o funcionamento de duas Máquinas de Turing (MT) escritas em Python, aplicadas sobre cadeias binárias. Ele permite verificar se um número binário:

- ✅ É um **palíndromo**
- ✅ É **divisível por 3**

Além disso, o sistema oferece:

- 🖼️ Geração automática de diagramas dos estados percorridos
- 🎞️ Criação de animações GIF com o caminho dos estados
- ⚙️ Execução paralela das duas MTs
- 📝 Log de execução detalhado com tempos e resultados

---

## 📁 Estrutura do Projeto

```
.
├── Visualizador.py               # Script principal (execução + visualização)
├── maquina_palindromo_mt.py     # Máquina de Turing para palíndromos
├── maquina_divisivel3_mt.py     # Máquina de Turing para divisibilidade por 3
├── log_execucao_mt.json         # Log automático gerado na execução
├── *.png / *.gif                # Diagramas e animações dos caminhos de estados
└── README.md                    # Documentação (este arquivo)
```

---

## ▶️ Como Executar

1. **Instale as dependências:**

```bash
pip install matplotlib graphviz imageio networkx
```

> 💡 Em sistemas Windows, instale também o [Graphviz](https://graphviz.org/download/) e adicione o executável ao PATH do sistema.

2. **Execute o script principal:**

```bash
python Visualizador.py
```

3. **Digite um número binário válido:**

```
Digite um número binário: 10101
```

---

## 📦 Resultados Gerados

Após a execução, o sistema criará:

- `Palindromo_caminho.png`: Caminho de estados da MT de palíndromo
- `Div3_animacao.gif`: Animação da MT que verifica divisibilidade por 3
- `log_execucao_mt.json`: Arquivo JSON com tempos, status, caminhos e nomes dos arquivos gerados

Exemplo de trecho do log:
```json
{
  "Palindromo": {
    "tempo": 0.018,
    "status": "ACEITA",
    "saida": "...",
    "caminho": ["q0", "q1", "q0", "q1", "q0", "q_accept"],
    "img": "Palindromo_caminho.png",
    "anim": "Palindromo_animacao.gif"
  },
  ...
}
```

---

## 🔍 Tecnologias Utilizadas

- Python 3.10+
- `multiprocessing` para execução paralela
- `matplotlib`, `networkx` e `imageio` para visualização
- `graphviz` para geração de diagramas de estados

---

## 📌 Aplicações Educacionais

Este projeto foi desenvolvido para fins didáticos e serve como base para:

- Estudo prático de Máquinas de Turing
- Visualização do comportamento de autômatos
- Integração de conceitos de paralelismo e análise de algoritmos

---

## 🧑‍💻 Autor

**[Seu Nome]**  
Curso: Engenharia / Ciência da Computação  
Data: Julho de 2025  
Instituição: [Nome da sua universidade]

---

## 📜 Licença

Este projeto é distribuído para fins educacionais e de pesquisa. Modificações e reutilizações são permitidas, desde que mencionada a fonte.
