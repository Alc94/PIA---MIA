# Tabla de -20 Cº a 40 Cº de 5 en 5 con su equivalente en Fahrenheit,
# en dos columnas alineadas
print(f"{'Celsius (Cº)':<15} {'Fahrenheit (Fº)':<15}")
for celsius in range(-20, 41, 5):
    fareh = (celsius * 9 / 5) + 32
    
    print(f"{celsius:<12.1f}{fareh:15.1f}") 