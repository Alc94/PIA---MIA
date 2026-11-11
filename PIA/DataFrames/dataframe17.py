import pandas as pd

# Comprobar si un objeto DataFrame está vacío con empty

alumnos = pd.read_csv('alumnos.csv')

print(alumnos.empty)

ejemplo = pd.DataFrame({})
print(ejemplo.empty)