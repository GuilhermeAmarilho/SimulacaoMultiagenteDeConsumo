# 🛒 Simulação Multiagente: Promoções e Comportamento do Cliente

## 📌 Descrição

Este projeto tem como objetivo simular o comportamento de clientes em um mercado, analisando como promoções influenciam decisões de compra e impactam o sistema como um todo.

A simulação utiliza o conceito de **Sistemas Multiagentes**, onde cada cliente é representado como um agente autônomo que toma decisões com base em suas características individuais.

---

## 🎯 Objetivo

Investigar como mudanças no comportamento individual dos clientes (nível micro) afetam o comportamento coletivo do sistema (nível macro), especialmente em relação a:

* Volume de vendas
* Consumo de produtos
* Esgotamento de estoque
* Compras por impulso

---

## 🧠 Modelo do Sistema

### 👥 Agentes

Os agentes representam os **clientes**, que possuem comportamentos diferentes:

* Cliente econômico → prioriza preço baixo
* Cliente impulsivo → compra mais com promoções
* Cliente fiel → mantém preferências fixas
* Cliente planejado → evita compras desnecessárias

---

### 🛍️ Ambiente

O ambiente representa um mercado com:

* Produtos
* Preços
* Promoções
* Estoque limitado

---

## ⚙️ Variáveis do Modelo

O sistema considera pelo menos três variáveis interdependentes:

* **Nível de desconto** → influencia a decisão de compra
* **Impulsividade do cliente** → afeta compras por promoção
* **Estoque** → limita a disponibilidade dos produtos

Variável adicional:

* **Orçamento do cliente**

---

## 🔁 Dinâmica da Simulação

A cada passo da simulação:

1. Clientes entram no mercado
2. Observam os produtos disponíveis
3. Avaliam preço, promoção e orçamento
4. Decidem comprar ou não
5. O estoque é atualizado
6. Os dados são registrados

---

## 📊 Métricas Coletadas

Durante a simulação, são coletados dados como:

* Total de vendas
* Faturamento
* Produtos vendidos em promoção
* Compras médias por cliente
* Estoque ao longo do tempo

---

## 🔬 Cenários de Simulação

Serão testados diferentes cenários, como:

* Sem promoção
* Promoções leves
* Promoções agressivas
* Diferentes perfis de clientes

---

## 📈 Resultados Esperados

A simulação permite observar:

* Aumento de vendas em promoções
* Picos de consumo
* Esgotamento de estoque
* Diferenças entre perfis de clientes
* Comportamentos emergentes

---

## 🛠️ Tecnologias Utilizadas

* Python
* Mesa (framework para simulação multiagente)

---

## 📦 Estrutura do Projeto

```mkd
project/
│── model/
│   ├── agents.py
│   ├── model.py
│
│── analysis/
│   ├── plots.py
│
│── run.py
│── README.md
```

---

## 🚀 Como Executar

* 1 nstale as dependências:

    ```bat
    pip install mesa
    ```

* 2 Execute o projeto:

    ```bat
    python run.py
    ```

---

## 📄 Entrega

Este projeto inclui:

* Código fonte da simulação
* Análise dos resultados
* Relatório em PDF

---

## 👨‍💻 Autor

Guilherme Amarilho

---

## 📚 Contexto Acadêmico

Trabalho desenvolvido para a disciplina de **Computação Científica**, com foco em **Simulação Multiagente**.
