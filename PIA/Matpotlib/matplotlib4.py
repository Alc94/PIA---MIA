import matplotlib.pyplot as plt
import pandas as pd

"""
El fichero bancos.csv contiene las cotizaciones de los principales
bancos de España con : 

    Empresa (nombre de la empresa), 
    Apertura (precio de la acción a la apertura de bolsa), 
    Máximo (precio máximo de la acción durante la jornada), 
    Mínimo (precio mínimo de la acción durante la jornada), 
    Cierre (precio de la acción al cierre de bolsa), 
    Volumen (volumen al cierre de bolsa). 

Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales de las cotizaciones de cierre de cada banco.
"""

def evolucion_cotizacion(datos, variable):
    
    fig, ax = plt.subplots()

    # dibujamos las series de cotizaciones por empresa
    datos.groupby('Empresa').plot(x = 'Fecha', y = variable, ax = ax)

    # añadimos el titulo
    plt.title(f'Evolucion de las cotizacones ({variable})')

    # añadimos la leyenda
    plt.legend(datos.groupby('Empresa').groups.keys())

    return ax

# Creamos un dataframe a partir del fichero csv
df_datos = pd.read_csv('bancos.csv')
# Convertimos la columna Fecha a formato datetime
df_datos["Fecha"] = pd.to_datetime(df_datos["Fecha"])
# Llamamos a la función para crear el gráfico
evolucion_cotizacion(df_datos, 'Cierre')
plt.show()
