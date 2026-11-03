import numpy as np

def f(numero):
    if numero <= 3:
        return 0
    elif numero <= 5:
        return 4
    elif numero <= 6:
        return 5
    elif numero <=7:
        return 6
    elif numero <= 9:
        return 8
    else:
        return 10

# Numpyzar la funcionar para que pueda iterar sobre un array de numpy
f_np = np.vectorize(f)

numeros = np.array([1, 5, 4, 7, 3, 9, 8, 6])

resultado = f_np(numeros)

print("Lista original: ", numeros)
print("Lista pasada por función: ", resultado)

