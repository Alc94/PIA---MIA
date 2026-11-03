import numpy as np
from sklearn.datasets import load_iris

datos = load_iris().data
resultado = load_iris().target

print(datos.shape)
print(resultado.shape)

# Enunciado: array sepal_length con 99 primeras filas y la 1 columna
sepal_length = datos[:99, 0]
print(sepal_length.shape)
print()

# Apartado 1: array petal_length con las primeras 99 filas y la 3 columna
petal_length = datos[:99, 2]
print(petal_length.shape)
print()

# Apartado 2: Array llamado x, juntando las 2 columnas de sepal_length y petal_length
x = np.column_stack((sepal_length, petal_length))
print(x.shape)
print()

# Apartado 3: Array llamado y, que contenga las 99 primeras filas del vector resultante
y = resultado[:99]
print(y.shape)
print()

# Apartado 4: Array llamado x, con las 99 primeras filas, la 1 columna y la 3 columna de datos
x1 = datos[:99, [0, 2]]
print(x1.shape)