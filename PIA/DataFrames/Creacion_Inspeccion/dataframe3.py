import pandas as pd

# Guardar los registros de un DataFrame en un archivo de formato CSV

ejemplo = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Marta'],
    'Edad': [25, 30, 28]
})

ejemplo.to_csv('ejemplo.csv', index = True)