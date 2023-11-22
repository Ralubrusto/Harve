import numpy as np
import matplotlib.pyplot as plt

altura = [1.8, 1.6, 2.1]
nomes = ['André', 'Augusto', 'Adalberto']

fig, ax = plt.subplots()

# Aqui um gráfico do tipo barra. A primeira lista deve vir com as categorias e a segunda, com os valores de cada uma
# No gráfico, cada categoria vira uma barra
ax.bar(nomes, altura, width=0.5)

ax.annotate('OIE', xy=(400, 800), xycoords='figure pixels')

plt.show()