import matplotlib.pyplot as plt
import pandas as pd

"""
Escribir una función que reciba una serie de Pandas con las notas
de los alumnos de un curso y devuelva un diagrama de cajas con las
notas. El diagrama debe tener el título "Distribución de notas".
"""
def diagrama_caja_notas(notas):

    # definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # dibujamos los sectores con las ventas a partir de la serie
    notas.plot(kind = 'box', ax = ax)
    # eliminamos las marcas del eje x
    plt.xticks([])

    # añadimos el titulo
    plt.title('Distribución de notas')

    return ax

notas = [4, 8, 7.5, 6, 5.5, 5.2, 3.5, 7.7, 3.2, 9, 6.8]
series_notas = pd.Series(notas)
diagrama_caja_notas(series_notas)

plt.show()