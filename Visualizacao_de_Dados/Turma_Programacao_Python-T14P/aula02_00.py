import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4]
x2 = [4, 3, 2, 1]
x3 = [5, 5, 5, 5]
x4 = [0, 0, 0, 0]
x5 = [3, 2, 3, 2]

fig, ax = plt.subplots()

# É possível plotar vários gráficos usando uma única chamada do ax.plot()
# A string que vem logo depois do valor indica o "Estilo" do plot
# - Pode indicar se a preferência é uma linha contínua ou se são apenas pontos isolados
ax.plot(x1, '+', x2, 'P', x3, 'h', x4, 'H', markersize=10)

# Segue a lista com os estilos para marcação de pontos isolados:
# 'o' - Círculo marker
# 'v' - Triângulo apontando para baixo
# '^' - Triângulo apontando para cima
# '<' - Triângulo apontando para esquerda
# '>' - Triângulo apontando para direita
# '8' - Octógono
# 's' - Quadrado
# 'p' - Pentágono
# '+' - Símbolo de adição '+'
# 'P' - Símbolo de adição '+' menos fino
# '*' - Asterisco
# 'h' - Hexágono
# 'H' - Hexágono 2
# 'x' - Letra X
# 'X' - Letra X menos fina
# 'd' - Losango 
# 'D' - Losango menos fino
