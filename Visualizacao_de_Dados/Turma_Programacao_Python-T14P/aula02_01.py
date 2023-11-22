import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4]
x2 = [3, 1, 2, 0]

fig, ax = plt.subplots()

# É possível plotar a linha junto com os marcadores
ax.plot(x1, marker='d', markersize=7, linestyle='--', color='b', label='Linha azul')

ax.plot(x2, marker='D', markersize=7, linestyle='-.', color='r', label='Linha vermelha')

# Estilos de linha:
# '-'  - Linha contínua
# '--' - Linha tracejada
# '-.' - Linha com traços e pontos intercalados
# ':'  - Linha pontilhada

plt.legend()
plt.show()
