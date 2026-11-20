import warnings
import pandas as pd

# Generar una representación de los elementos de un DataFrame con applymap
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')
print(numerico, '\n')

# applymap aplica una función a CADA elemento del DataFrame
# Nota: desde pandas 2.1 está deprecado y su sustituto es DataFrame.map
def formato(x):
    return f'{x:.1f}'

try:
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', FutureWarning)
        resultado = numerico.applymap(formato)
except AttributeError:
    # En versiones recientes de pandas applymap ya no existe
    resultado = numerico.map(formato)

print(resultado, '\n')
print(resultado.dtypes)
