import pandas as pd

# Calcular el producto punto entre dos objetos DataFrame con la función dot
a = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['x', 'y', 'z'])
b = pd.DataFrame([[1, 0], [0, 1], [1, 1]], index=['x', 'y', 'z'], columns=['p', 'q'])
print(a, '\n')
print(b, '\n')

# Las columnas del primero deben coincidir con el índice del segundo
print(a.dot(b), '\n')

# Con el operador @
print(a @ b, '\n')

# Un DataFrame por su transpuesta
print(a.dot(a.T))
