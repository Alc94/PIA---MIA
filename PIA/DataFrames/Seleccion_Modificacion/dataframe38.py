import pandas as pd

# Seleccionar registros donde se cumpla una condición para valores de una columna
alumnos = pd.read_csv('../datos/alumnos.csv')

# Condicion siempre, notas aprobadas
aprobados = alumnos[alumnos['nota'] >= 5]
print(aprobados, '\n')

# Igualdad con un texto, en este caso devuelve un DataFrames vacio
print(alumnos[alumnos['nombre'] == 'Ana'], '\n')

# Con .loc, eligiendo ademas las columnas a mostrar
print(alumnos.loc[alumnos['nota'] >= 5, ['nombre', 'nota']], '\n')

# Varias condiciones: & (y), | (o), ~ (no)
print(alumnos[(alumnos['nota'] >= 5) & (alumnos['edad'] < 22)],'\n')
print(alumnos[(alumnos['nota'] < 5) | (alumnos['edad'] > 25)],'\n')
print(alumnos[~(alumnos['nota'] >= 5)])