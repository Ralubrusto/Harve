import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 3000)
y = x**2 

plt.plot(x, y)

plt.xlabel("Este é meu eixo x")
plt.ylabel("Estes são meus valores")
plt.title('TÍTULOOOOOOOOO')

plt.grid()
plt.show()