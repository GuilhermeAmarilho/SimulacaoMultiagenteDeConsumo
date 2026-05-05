# Simulação Multiagente de Consumo em um Mercado

## 📌 Descrição

Este projeto consiste em uma simulação multiagente desenvolvida em Python utilizando a biblioteca MESA. O objetivo é analisar o comportamento de consumo de clientes em um mercado, considerando fatores como promoção, preço e influência social.

A simulação permite observar como decisões individuais dos agentes impactam o comportamento coletivo do sistema, evidenciando padrões emergentes ao longo do tempo.

---

## 🧠 Modelo

O sistema é composto por agentes que representam clientes, cada um com características próprias:

- Dinheiro disponível
- Nível de interesse
- Tipo de comportamento:
  - Econômico
  - Impulsivo
  - Regular

Além disso, o modelo considera variáveis globais:

- Promoção
- Preço do produto
- Influência social

A cada rodada, os agentes decidem se realizam uma compra com base nessas variáveis.

---

## ⚙️ Simulação

A simulação foi configurada com:

- 50 agentes
- 100 rodadas
- 20 execuções por cenário

Foram analisados os seguintes cenários:

- Sem promoção
- Promoção média
- Promoção alta
- Sem influência social

---

## 📊 Resultados

Os resultados mostram que o sistema apresenta:

- Alto consumo inicial
- Redução progressiva das compras ao longo do tempo
- Comportamento emergente decorrente da interação entre agentes

O gráfico gerado demonstra a evolução das compras em diferentes cenários.

---

## 🚀 Como executar

1. Criar um ambiente virtual:

```bash
    python -m venv venv_CC
```

2. Ativar o ambiente:

```bash
    venv_CC\Scripts\activate
```

3. Instalar dependências:

```bash
    pip install mesa matplotlib
```

4. Executar o projeto:

```bash
    python run.py
```

---

## 📁 Estrutura do projeto

```
.
├── agents.py
├── model.py
├── run.py
├── resultados/
└── README.md
```

---

## 📌 Observações

O modelo não considera reposição de renda dos agentes, o que resulta na redução progressiva das compras ao longo das rodadas. Esse comportamento é proposital para evidenciar padrões emergentes no sistema.

---

## 👨‍💻 Autor

### Guilherme Amarilho