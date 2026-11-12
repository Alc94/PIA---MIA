import pandas as pd

# Crea un DataFrame a partir de uno existente tomando alguna de las columnas del DataFrame existente
alumnos = pd.read_csv('../datos/alumnos.csv')
# Sin el pd.DataFrame devolveria una Series
df_nombre1 = pd.DataFrame(alumnos['nombre'])
print(df_nombre1)

# Otras formas de crear un DataFrame con una o dos columnas
df2 = alumnos[['nombre']]
print(df2)

# Con varias columnas a la vez
df3 = alumnos[['nombre', 'edad']]
print(df3)

# Con .to_frame(), convierte una Series en DataFrames
df4 = alumnos['nombre'].to_frame()
print(df4)
print(type(df4))

# Y con .loc, realizamos slicing para seleccionar las columnas que queremos
# Escogemos con ':' todas las filas y entre corchetes, las columnas
df5 = alumnos.loc[:, ['nombre', 'nota']]
print(df5)