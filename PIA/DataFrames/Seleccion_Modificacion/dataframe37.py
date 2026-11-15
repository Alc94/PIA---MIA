import pandas as pd

# Seleccionar registros donde los valores de una columna estén en un rango
alumnos = pd.read_csv('../datos/alumnos.csv')

# Con between (se incluye ambos extremos)
notables = alumnos[alumnos['nota'].between(7, 9)]
print(notables)

# Mediante con dos condiciones (cada una entre parentesis)
notables1 = alumnos[(alumnos['nota'] >= 7) & (alumnos['nota'] <= 9)]
print(notables1)

# Con .loc, y quedandote solo con algunas columnas
print(alumnos.loc[alumnos['nota'].between(7, 9), ['nombre', 'nota']])