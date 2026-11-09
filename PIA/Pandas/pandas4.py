import pandas as pd

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 4, 5, 8, 9])

""" Usar operadores relacionales para comparar objetos Series """
# Cada comparación devuelve una Series de booleanos
print("Igual:\n", s1 == s2)
print("Mayor:\n", s1 > s2)
print("Menor:\n", s1 < s2)
print("Distinto:\n", s1 != s2)
