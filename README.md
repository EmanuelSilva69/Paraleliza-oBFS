#  Visualizador de Máquinas de Turing — Palíndromo e Divisibilidade por 3

Este projeto simula e visualiza o funcionamento de duas Máquinas de Turing (MT) escritas em Python, aplicadas sobre cadeias binárias. Ele permite verificar se um número binário:

-  É um **palíndromo**
-  É **divisível por 3**

Além disso, o sistema oferece:

- 🖼 Geração automática de diagramas dos estados percorridos
- 🎞 Criação de animações GIF com o caminho dos estados
- ⚙ Execução paralela das duas MTs
-  Log de execução detalhado com tempos e resultados

---

##  Estrutura do Projeto

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

## ▶ Como Executar

1. **Instale as dependências:**

```bash
pip install matplotlib graphviz imageio networkx
```

2. **Execute o script principal:**

```bash
python Visualizador.py
```

3. **Digite um número binário válido:**

```
Digite um número binário: 10101
```

---

##  Resultados Gerados

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

##  Tecnologias Utilizadas

- Python 3.10+
- `multiprocessing` para execução paralela
- `matplotlib`, `networkx` e `imageio` para visualização
- `graphviz` para geração de diagramas de estados

---

##  Aplicações Educacionais

Este projeto foi desenvolvido para fins didáticos e serve como base para:

- Estudo prático de Máquinas de Turing
- Visualização do comportamento de autômatos
- Integração de conceitos de paralelismo e análise de algoritmos

---

## 🧑‍💻 Autor

**Emanuel Lopes Silva**  
Curso: Engenharia  da Computação  
Data: Julho de 2025  
Instituição: Universidade Federal do Maranhão

---

## 📜 Licença

Este projeto é distribuído para fins educacionais e de pesquisa. Modificações e reutilizações são permitidas, desde que mencionada a fonte.
Copyright/License
Este material é resultado de um trabalho acadêmico para a disciplina EECP0050 -
Linguagens Formais e Automatos, sob a orientação do professor Dr. THALES LEVI AZEVEDO
VALENTE, semestre letivo 2025.1, curso Engenharia da Computação, na
Universidade Federal do Maranhão (UFMA). Todo o material sob esta licença é
software livre: pode ser usado para fins acadêmicos e comerciais sem nenhum custo.
Não há papelada, nem royalties, nem restrições de "copyleft" do tipo GNU. Ele é
licenciado sob os termos da Licença MIT, conforme descrito abaixo, e, portanto, é
compatível com a GPL e também se qualifica como software de código aberto. É de
domínio público. Os detalhes legais estão abaixo. O espírito desta licença é que você
é livre para usar este material para qualquer finalidade, sem nenhum custo. O único
requisito é que, se você usá-los, nos dê crédito.
Licenciado sob a Licença MIT. Permissão é concedida, gratuitamente, a qualquer
pessoa que obtenha uma cópia deste software e dos arquivos de documentação
associados (o "Software"), para lidar no Software sem restrição, incluindo sem
limitação os direitos de usar, copiar, modificar, mesclar, publicar, distribuir,
sublicenciar e/ou vender cópias do Software, e permitir pessoas a quem o Software
é fornecido a fazê-lo, sujeito às seguintes condições:
Este aviso de direitos autorais e este aviso de permissão devem ser incluídos em todas
as cópias ou partes substanciais do Software.
O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE
QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO MAS NÃO SE
LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM
DETERMINADO FIM E NÃO INFRINGÊNCIA. EM NENHUM CASO OS
AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO
RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA
RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, TORT OU OUTRA
FORMA, DECORRENTE DE, FORA DE OU EM CONEXÃO COM O
SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.
Para mais informações sobre a Licença MIT: https://opensource.org/licenses/MIT

