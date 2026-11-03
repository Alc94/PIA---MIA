import numpy as np

def f(num):
    return num * 2 + 1


numeros = np.array([1, 5, 4, 7, 3, 9, 8, 6])

resultado = f(numeros)

print("Lista original: ", numeros)
print("Lista modificada: ", resultado)