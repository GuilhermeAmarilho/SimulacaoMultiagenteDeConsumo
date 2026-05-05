from mesa import Agent
import random


class ClienteAgent(Agent):
    def __init__(self, model, dinheiro, interesse, tipo):
        super().__init__(model)

        self.dinheiro = dinheiro
        self.interesse = interesse
        self.tipo = tipo
        self.comprou = False

    def step(self):
        # comportamento por tipo
        if self.tipo == "economico":
            chance_de_compra = self.interesse * 0.5
        elif self.tipo == "impulsivo":
            chance_de_compra = self.interesse * 1.2
        else:
            chance_de_compra = self.interesse

        # promoção
        chance_de_compra += self.model.promocao

        # influência social
        if self.model.usar_influencia:
            influencia_social = self.model.total_compras / self.model.n_clientes
        else:
            influencia_social = 0

        chance_de_compra += influencia_social

        # limitar entre 0 e 1
        chance_de_compra = max(0, min(1, chance_de_compra))

        # decisão
        sorteio = random.random()

        if sorteio < chance_de_compra and self.dinheiro >= self.model.preco_produto:
            self.comprou = True
            self.dinheiro -= self.model.preco_produto
        else:
            self.comprou = False