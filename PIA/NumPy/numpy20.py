import numpy as np

np.random.seed(3)
ages = np.random.randint(18, 70, size=200)  # Edades de 200 personas
income = np.random.normal(50000, 15000, size=200)  # Ingresos anuales en un rango normal alrededor de 50,000
education_years = np.random.randint(0, 20, size=200)  # Años de educación formal


""" Apartado 1: Calcula la correlacion entre los años de educacion y los ingresos """
correlacion = np.corrcoef(education_years, income)
print(f"Correlacion entre años de educacion y los ingresos: ", correlacion)

""" Apartado 2: Divide a las personas en grupos de edades (18-30, 31-45, 46-60, 61+)
y calcula el ingreso promedio por grupo """
g1 = (ages >= 18) & (ages <= 30)
g2 = (ages >= 31) & (ages <= 45)
g3 = (ages >= 46) & (ages <= 60)
g4 = ages >= 61

print("Grupo de 18-30:", round(income[g1].mean(), 2))
print("Grupo de 31-45:", round(income[g2].mean(), 2))
print("Grupo de 46-60:", round(income[g3].mean(), 2))
print("Grupo de 61 o mas:", round(income[g4].mean(), 2))


""" Apartado 3: Encuentra el percentil 90 de ingresos y determina
cuántas personas ganan por encima de ese valor """
p90 = np.percentile(income, 90)
print("Percentil 90: ", p90)

por_encima = np.sum(income > p90)
print("Personas por encima: ", por_encima)


""" Apartado 4: Agrupa los datos en función del número de años de educación y 
calcula el promedio de ingresos para cada grupo """
for anios in np.unique(education_years):
    media = income[education_years == anios].mean()
    print(f"{anios} años de educacion: {round(media, 2)}")