import numpy as np
import matplotlib.pyplot as plt

# Plotar 3 gráficos (1 linha e 3 colunas):
# - O primeiro sendo 2 * x**2 -------- EM VERDE
# - O primeiro sendo 3 * x**3 -------- EM AZUL
# - O primeiro sendo 4 * x    -------- EM VERMELHO

x = np.linspace(-3, 3, 3000)
y1 = 2 * x**2
y2 = 3 * x**3 
y3 = 4 * x

# É possível dividir uma imagem em mais gráficos, basta considerar a imagem como uma matriz de gráficos
# Passamos para a função plt.subplots o número de linhas e o número de colunas dessa matriz
fig, ax = plt.subplots(1, 3)

# Depois para plotar em cada local individualmente acessamos a variável ax como uma lista
ax[0].plot(x, y1, color='green', label='2 * x**2')
ax[0].set_ylabel("Eixo y")
ax[0].grid()

ax[1].plot(x, y2, color='blue', label='3 * x**3')
ax[1].grid()

ax[2].plot(x, y3, color='red', label='4 * x')
ax[2].grid()

plt.show()