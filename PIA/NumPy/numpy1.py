import numpy as np

primos = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
print(primos)

# Apartado 1: Mostrar el ultimo elemento
ultimoElemento = primos[-1]
print(ultimoElemento)

# Apartado 2: Mostrar el tercer elemento
tercerElemento = primos[2]
print(tercerElemento)

# Apartado 3: Mostrar el ultimo y tercer elemento
ultimoYtercer = primos[[-1, 2]]
print(ultimoYtercer)

# Apartado 4: Mostrar del segundo al quinto elemento
segundoAlQuinto = primos[1:5]
print(segundoAlQuinto)

# Apartado 5: Mostrar el segundo y quinto elemento
segundoYQuinto = primos[[1, 4]]
print(segundoYQuinto)

# Apartado 6: Mostrar el ultimo y penultimo elemento
ultimoYPenultimo = primos[[-1, -2]] # [-2:]
print(ultimoYPenultimo)