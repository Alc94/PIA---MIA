import pandas as pd
import matplotlib.pyplot as plt

"""
El fichero titanic.csv contiene información sobre los pasajeros del Titanic.
Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.

Diagrama de sectores con los fallecidos y supervivientes.
Histograma con las edades.
Diagrama de barras con el número de personas en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
"""

# Creamos un dataframe a partir del fichero csv
df_titanic = pd.read_csv('titanic.csv')
# Creamos la figura y los ejes
fig, ax = plt.subplots()
# Diagrama de sectores de falleccidos y supervivientes
df_titanic.Survived.value_counts().plot(kind = "pie", labels = ["Muertos", "Supervivientes"], title = "Distribución de supervivientes")
plt.show()

print()

# Histograma de edades
df_titanic.Age.plot(kind = "hist", title = "Histograma de edades")
plt.show()

print()

# Diagrama de barras con el número de personas de cada clase
df_titanic.Pclass.value_counts().plot(kind = "bar", title = "Número de personas por clase")
plt.show()

print()

# Diagrama de barras con el número de personas fallecidas y supervivientes de cada clase
df_titanic.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", title = "Número de personas fallecidas y supervivientes por clase")
plt.show()

print()

# Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas de cada clase
df_titanic.groupby(["Pclass", "Survived"]).size().unstack().plot(kind = "bar", stacked = True, title = "Número de personas fallecidas y supervivientes por clase")
plt.show()