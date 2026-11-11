import pandas as pd

# Crear un objeto de la clase DataFrame
ejemplo = pd.DataFrame([1, 2, 3, 4, 5], columns=['Numeros'])
print(ejemplo)

# Desde un diccionario (la forma más habitual)
ejemplo2 = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Marta'],
    'Edad': [25, 30, 28]
})
print(ejemplo2)