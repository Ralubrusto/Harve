import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 3000)
y1 = x**2
y2 = x**3 

fig, ax = plt.subplots()

ax.plot(x, y1, color='red', label='x**2')
ax.plot(x, y2, color='green', label='x**3')
ax.set_ylabel("Eixo y")
ax.set_xlabel("Eixo x")
ax.set_title("Título")

ax.grid()
ax.legend()

plt.show()