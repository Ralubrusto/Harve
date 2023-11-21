import numpy as np
import matplotlib.pyplot as plt

altura = [1.8, 1.6, 2.1]
nomes = ['André', 'Augusto', 'Adalberto']

fig, ax = plt.subplots()

ax.bar(nomes, altura, width=0.5)

ax.annotate('OIE', xy=(400, 800), xycoords='figure pixels')


ax.set_ylabel("Eixo y")
ax.set_xlabel("Eixo x")
ax.set_title("Título")

# ax.grid()
# ax.legend()

plt.show()