""" 
3. Dado un conjunto data de observaciones, ajusta una normal usando la media y desviación poblacional del conjunto. Crea una función normal_tasks(data, x, p) que:
Cree un NormalDist ajustado a data.
Calcule la probabilidad P(X <= x) (CDF).
Calcule el percentil (inversa) inv_cdf(p): el valor y tal que P(X <= y) = p.
Devuelva además el z-score de x usando (x - mean)/stdev.


Usa statistics.NormalDist.

"""

import statistics
from statistics import NormalDist

def normal_tasks(data, x, p):

    if not data:
        raise ValueError("La lista no debe de estar vacía...")
    if any(d < 0 or d > 10 for d in data):
        raise ValueError("Los valores deben ser mínimo 0 y máximo 10...")
    if not 0 < p < 1:
        raise ValueError("El valor 'p' debe estar entre 0 y 1...")

    media = statistics.mean(data)
    pstdev = statistics.pstdev(data)

    if pstdev == 0:
        raise ValueError("La desviacion es 0: no se puede ajustar una normal...")

    # Con NormalDist, se crea (mediante con la media y la desviación tipica) una distribucion normal.
    # Se crea un objeto con metodos para hacer calculos sobre dicha campana (Campana de Gauss)
    dist = NormalDist(media, pstdev)

    return {
        # Cumulative Distribution Function (Funcion de distribución acumulada):
        # Cuál es la probabilidad de que un valor sea menor o igual que x ?
        # Es el área bajo la campana a la izquierda de x. El resultado va siempre de 0 a 1.
        # Das un valor 'x' y obtienes una probabilidad
        "cdf": dist.cdf(x),

        # Operación inversa de la CDF
        # Das una probabilidad 'p' y obtienes el valor 'y'
        # Ejemplo: inv_cfd(0.95) te dice qué valor deja el 95% de los datos por debajo.
        # Por eso se le llama también percentil (aquí, el percentil 95)
        "inv_cdf": dist.inv_cdf(p),

        # Puntuación Z: Medida estadística que indica cuántas desviaciones estándar está un valor
        # específico por encima o por debajo de la media de un conjunto de datos.
        # Si Z = 0 , el valor es exactamente igual al promedio
        # Si Z > 0 , el valor está por encima de la media
        # Si Z < 0 , el valor está por debajo de la media
        # Si una puntuación Z es mayor que 2, significa que el dato está dos desviaciones estandar arriba de la media
        "z_score": (x - dist.mean) / dist.stdev,
    }

if __name__ == "__main__":

    notas = [0, 6, 7, 3, 4, 6, 4, 5, 2, 10, 1, 1]

    print(normal_tasks(notas, 5, 0.90))
    
    try:

        print(normal_tasks([], 6, 0.5))

    except ValueError as e:
        print("Error: ", e)

    try:

        print(normal_tasks([-1, 2, 6, 8, -1], 3, 0.3))

    except ValueError as e:
        print("Error: ", e)

    