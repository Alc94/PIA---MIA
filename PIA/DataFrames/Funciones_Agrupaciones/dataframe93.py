import pandas as pd

# Verificar con equals si dos objetos DataFrame contienen los mismos elementos
alumnos = pd.read_csv('../datos/alumnos.csv')

copia = alumnos.copy()
print(alumnos.equals(copia))          # True: mismos valores, etiquetas y tipos

# Si se modifica un valor, ya no son iguales
copia.loc[0, 'nota'] = 10
print(alumnos.equals(copia))          # False

# equals compara también los tipos de datos
a = pd.DataFrame({'x': [1, 2, 3]})
b = pd.DataFrame({'x': [1.0, 2.0, 3.0]})
print(a.equals(b))                    # False: int64 frente a float64
print((a == b).all().all())           # True: los valores sí coinciden
