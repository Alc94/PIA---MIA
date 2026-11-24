import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
Escribir un programa que pregunte al usuario por las ventas de un rango de años
 y muestre por pantalla un diagrama de líneas con la evolución de las ventas.
"""

año_inicial = int(input("Año inicial: "))
año_finalizacion = int(input("Año finalización: "))

ventas = {}

for i in range(año_inicial, año_finalizacion + 1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) + ': '))

fig, ax = plt.subplots()

ax.plot(ventas.keys(), ventas.values())

plt.show()