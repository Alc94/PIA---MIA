import pandas as pd

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

""" Operaciones aritmeticas basicas (suma, resta, multiplicacion y division)
sobre objetos Series """
# Las operaciones se hacen elemento a elemento, alineando por índice
print("Suma:\n", s1 + s2)
print()
print("Resta:\n", s1 - s2)
print()
print("Multiplicación:\n", s1 * s2)
print()
print("División:\n", s1 / s2)
