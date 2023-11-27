# Normalmente utilizamos a biblioteca com o apelido "plt"
import matplotlib.pyplot as plt

# Nos casos mais básicos podemos usá-la para plotar uma lista de valores
x1 = [1, 5, 2, 5]
x2 = [0, 4, 1, 9]

# O comando plt.plot() plota gráficos de linha
plt.plot(x1)

# Se você quiser que ele plote apenas os pontos (sem interligá-los) faça como o comando abaixo
plt.plot(x2, '*')

# Configurações para dar nomes aos eixos e ao gráfico
plt.xlabel("Nome do eixo X")
plt.ylabel("Nome do eixo Y")
plt.title('Título do gráfico')

# Este comando mostra efetivamente o gráfico pra ti. Note que ele pausa a execução do seu código
plt.show()

# Este print abaixo só será executado depois que você fechar a janela com o seu gráfico
print("Acabou!")