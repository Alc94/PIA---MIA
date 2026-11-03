import numpy as np

matriz = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Apartado 1: Multiplicar cada elemento por si mismo
multiplicacion = matriz * matriz # Ó np.multiply(matriz, matriz)
print(multiplicacion)
print()

# Apartado 2: Multiplicar la matriz por si misma
multiplicado = matriz @ matriz # Ó np.matmul(m, m)
print(multiplicado)