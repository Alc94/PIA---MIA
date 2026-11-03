import numpy as np

m = np.array([[1, 4, 6, 5],
              [4, 1, 7, 3],
              [2, 9, 1, 2],
              [6, 3, 1, 1]])
print(m)
print()

# Apartado 1
primer = m[1][2] # m[1, 2]
print(primer)
print()

# Apartado 2
segundo = m[2][:] # m[2, :] ó m[2]
print(segundo)
print()

# Apartado 3
tercero = m[:, 1]
print(tercero)
print()

# Apartado 4
cuarto = m[:, 1:3]
print(cuarto)
print()

# Apartado 5
quinto = m[1:3]
print(quinto)
print()

# Apartado 6
sexto = m[:, -1]
print(sexto)
print()

# Apartado 7
print(m[:, [1, 3]]) # Columnas 2 y 4
print(m[[0, 2]]) # Filas 1 y 3
print()

# Apartado 8
print(m[0:3, 1:3]) # De la 2 a la 3 columna y de la 1 hasta la 3 fila
print()

# Apartado 9
print(m[:, 1:-1]) # Todas las columnas excepto la primera y la ultima
print()

# Apartado 10
print(m[1: -1]) # Todas las filas excepto la primera y la ultima
print()

# Apartado 11
print(m[1:-1, 1:-1]) # Todas las columnas menos la primera y la ultima
        # Y todas las filas menos la primera y la ultima
print()

# Apartado 12
print("A B C D")
for n in m:
    print(*n)