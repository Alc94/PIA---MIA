import numpy as np

matriz = np.array([[1, 4, 6, 5],
                    [4, 1, 7, 3],
                    [2, 9, 1, 2],
                    [6, 3, 1, 1]])

# Apartado 1: Sumar a cada elemento, 10
suma = np.add(matriz, 10)
print(suma)
print()

# Apartado 2: Sumar a cada elemento 10 y dividirlo despues entre 2
sumaYDivision = np.divide(np.add(matriz, 10), 2)
print(sumaYDivision)
print()

# Apartado 3: Sumar a cada elemento 10 usando operadores
sumado = matriz + 10
print(sumado)
print()

# Apartado 4: Sumar a cada elemento 10 y dividirlo despues entre 2 usando operadores
sumadoYDividido = (matriz + 10) / 2
print(sumadoYDividido)