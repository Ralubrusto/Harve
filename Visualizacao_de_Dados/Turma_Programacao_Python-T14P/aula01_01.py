# Biblioteca para lidar com dados numéricos: numpy (apelido comum np)
import numpy as np
import matplotlib.pyplot as plt

# Numpy usa arrays ao invés de listas, mas que podem ser usados para plotar gráficos da mesma maneira

# Assim criamos um array
x1 = np.array([1, 5, 2, 5])
x2 = np.array([0, 4, 1, 9])

# E a forma de plotar é exatamente a mesma de antes
plt.plot(x1)
plt.plot(x2, 'x')  # Ao usar 'x' no lugar de 'o' os pontos ficarão com outro formato no gráfico

plt.xlabel("Nome do eixo X")
plt.ylabel("Nome do eixo Y")
plt.title('Título do gráfico')

plt.grid() # Ativa a grade para facilizar a identificação dos valores
plt.show()