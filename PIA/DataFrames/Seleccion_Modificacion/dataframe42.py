import pandas as pd

# Recorrer cada una de las columnas de un objeto DataFrame con items
alumnos = pd.read_csv('../datos/alumnos.csv')

for nombre, columna in alumnos.items():
    print('Columna:', nombre)
    print(columna)
    print()
    
# Tipo y numero de valores distintos en cada columna
for nombre, columna in alumnos.items():
    print(nombre, columna.dtype, columna.nunique())
    
print()
    
# Media solo de las columnas numericas
for nombre, columna in alumnos.items():
    if pd.api.types.is_numeric_dtype(columna):
        print(f"Media de {nombre}: {columna.mean():.2f}")