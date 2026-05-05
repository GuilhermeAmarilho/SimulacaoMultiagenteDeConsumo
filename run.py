from model import MercadoModel
import matplotlib.pyplot as plt
import statistics


def rodar_simulacao(n_clientes, rodadas, promocao, preco, usar_influencia, repeticoes=20):
    medias = []
    ultimo_historico = []

    for _ in range(repeticoes):
        modelo = MercadoModel(n_clientes)

        modelo.promocao = promocao
        modelo.preco_produto = preco
        modelo.usar_influencia = usar_influencia

        historico = []

        for _ in range(rodadas):
            modelo.step()
            total = sum(1 for c in modelo.agentes if c.comprou)
            historico.append(total)

        media = sum(historico) / len(historico)
        medias.append(media)

        ultimo_historico = historico

    media_final = sum(medias) / len(medias)
    variancia = statistics.variance(medias)

    return ultimo_historico, media_final, variancia


# parametros
n_clientes = 50
rodadas = 100


# cenarios
sem_promocao, m1, v1 = rodar_simulacao(n_clientes, rodadas, 0.0, 10, True)
promo_media, m2, v2 = rodar_simulacao(n_clientes, rodadas, 0.3, 10, True)
promo_alta, m3, v3 = rodar_simulacao(n_clientes, rodadas, 0.7, 10, True)
sem_influencia, m4, v4 = rodar_simulacao(n_clientes, rodadas, 0.3, 10, False)


#  resultados
print("=== MEDIAS DE COMPRAS ===")
print(f"Sem promoção: {m1:.2f} | Variância: {v1:.4f}")
print(f"Promoção média: {m2:.2f} | Variância: {v2:.4f}")
print(f"Promoção alta: {m3:.2f} | Variância: {v3:.4f}")
print(f"Sem influência: {m4:.2f} | Variância: {v4:.4f}")


# gráfico
plt.plot(sem_promocao, label="Sem promoção")
plt.plot(promo_media, label="Promoção média (0.3)")
plt.plot(promo_alta, label="Promoção alta (0.7)")
plt.plot(sem_influencia, label="Sem influência social")

plt.xlabel("Rodadas")
plt.ylabel("Número de compras")
plt.title("Comparação de cenários")
plt.legend()

# salvar imagem
plt.savefig("resultados/grafico.png")

plt.show()