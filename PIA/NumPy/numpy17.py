import matplotlib.pyplot as plt
import numpy as np

def dibujar(x, titulo):
    y = 3*(1 - x)**2 * np.exp(-x**2) - 10*(x/5 - x**3)*np.exp(-x**2) - 1./3*np.exp(-(x + 1)**2)
    figure = plt.figure(figsize=(8, 8))
    axes = figure.add_subplot()
    axes.plot(x, y)
    axes.set_title(titulo)

# Apartado 1: array float con los 7 valores originales
dibujar(np.array([-3, -2, -1, 0, 1, 2, 3], dtype=float), "7 valores (array float)")

# Apartados 2 a 6: linspace con distinto número de puntos
for n in [10, 20, 40, 60, 100]:
    dibujar(np.linspace(-3, 3, n), f"{n} valores entre [-3, 3]")

plt.show()   # abre todas las figuras a la vez