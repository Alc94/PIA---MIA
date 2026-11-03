import numpy as np

matriz = np.arange(168).reshape(7, 8, 3) # 7 filas, 8 columnas y 3 capas
print(matriz)
print()

# Capa roja
roja = matriz[2:5, 2:6, 0]
print(roja)
print()

# Capa verde
verde = matriz[2:5, 2:6, 1]
print(verde)
print()

# Capa azul
azul = matriz[2:5, 2:6 , 2]
print(azul)
