import numpy as np

# Apartado 1
primos = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], dtype=np.float32)
print(primos)

# Apartado 2
numeros1 = np.arange(100, 200)
print(numeros1)

# Apartado 3
numeros2 = np.array(range(100, 200))
print(numeros2)


"""
La principal diferencia que range(100, 200) es un objeto
y arange() es un metodo de la libreria de NumPy. Es por ello
que al mostrar range, muestra como tal el objeto.

Tendremos que utilizar el propio metodo de NumPy para poder
transformar el objeto en un array de NumPy
"""