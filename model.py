from mesa import Model
from agents import ClienteAgent
import random


class MercadoModel(Model):
    def __init__(self, n_clientes):
        super().__init__()

        self.n_clientes = n_clientes
        self.agentes = []

        # variáveis globais
        self.promocao = 0.3
        self.preco_produto = 10
        self.usar_influencia = True

        # controle de compras
        self.total_compras = 0

        tipos = ["economico", "impulsivo", "regular"]

        # criação dos agentes
        for _ in range(self.n_clientes):
            dinheiro = random.randint(50, 200)
            interesse = random.random()
            tipo = random.choice(tipos)

            cliente = ClienteAgent(
                model=self,
                dinheiro=dinheiro,
                interesse=interesse,
                tipo=tipo
            )

            self.agentes.append(cliente)

    def step(self):
        self.total_compras = 0

        for agente in self.agentes:
            agente.step()

            if agente.comprou:
                self.total_compras += 1