import numpy as np

temperaturas = np.array([10.2, 10.7, 13.3, 15.8, 19.3, 23.6, 26, 25.9, 22.8, 19.1, 13.9, 10.8 ])

# Apartado 1: Mostrar las temperaturas que sea mayor que 20
mayor20 = temperaturas[temperaturas > 20]
print(mayor20)
print()

# Apartado 2: Mostrar las temperaturas menor que 11
menor11 = temperaturas[temperaturas < 11]
print(menor11)

# Apartado 3: Mostrar las temperaturas mayor que 20 y menor que 11
mayor20YMenor11 = temperaturas[(temperaturas > 20) | (temperaturas < 11)]
# Tambien valdria temperaturas[np.logical_or(temperaturas > 20, temperaturas < 11)]
print(mayor20YMenor11)