import matplotlib.pyplot as plt

"""
Escribir una función que reciba una diccionario con las notas
de las asignaturas de un curso y una cadena con el nombre de
un color y devuelva un diagrama de barras de las notas en el color dado.
"""

def diagrama_barras_notas(notas, color):

    # definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()

    # Dibujamos las barras con las notas a partir del diccionario
    ax.bar(notas.keys(), notas.values(), color = color)

    # devolvemos un objeto con los ejes y las barras que contienen
    return ax

notas = {'Programación': 9, 'Mates':6.5, 'Economía': 4, 'Historia': 8}
diagrama_barras_notas(notas, 'orange')

plt.show()

