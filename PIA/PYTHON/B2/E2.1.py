# Estadísticas de una lista de notas: media, máximo, mínimo
# y cuántas aprobadas, sin usar statistics.

notas = [1, 4, 6, 3, 10, 9.5, 3,5]

maximo, minimo, = max(notas), min(notas)
media = 0
contador = 0

for i in notas:
    media += i
    
    if i > 4:
        contador += 1
    
media /= len(notas)

print(f'La nota MAXIMA es de {maximo}, la nota minima es de {minimo}, el numero de aprobados es de {contador} y la nota media es de {media:.2f}')
