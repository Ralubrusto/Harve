import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 3000)
y1 = 2 * x**2
y2 = 3 * x**3 
y3 = 4 * x

# Plotar 3 gráficos (1 linha e 3 colunas):
# - O primeiro sendo 2 * x**2 -------- EM VERDE
# - O primeiro sendo 3 * x**3 -------- EM AZUL
# - O primeiro sendo 4 * x    -------- EM VERMELHO

fig, ax = plt.subplots(1, 3)

ax[0].plot(x, y1, color='green', label='2 * x**2')
ax[0].set_ylabel("Eixo y")

ax[1].plot(x, y2, color='blue', label='2 * x**2')

ax[2].plot(x, y3, color='red', label='2 * x**2')

# ax.set_ylabel("Eixo y")
# ax.set_xlabel("Eixo x")
# ax.set_title("Título")

# ax.grid()
# ax.legend()
ax.legend()
# plt.tight_layout()
plt.show()