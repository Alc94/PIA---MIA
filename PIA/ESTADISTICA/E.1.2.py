""" Escribe compare_means(nums) que reciba una lista de números
positivos y devuelva un dict con: media aritmética (mean), 
media armónica (harmonic_mean), media geométrica (geometric_mean),
desviación poblacional (pstdev) y coeficiente de variación 
(cv = pstdev/mean). """

import statistics

def compare_means(nums):

    if not nums:
        raise ValueError("La lista no puede estar vacía...")

    if any(n <= 0 for n in nums):
        raise ValueError("La lista no puede contener números negativos o 0...")

    # Aqui se calcula la media de la tupla
    mean = statistics.mean(nums)
    # Y aqui se calcula la desviacion típica (desviación poblacional)
    pstdev = statistics.pstdev(nums)

    return {
        "mean": mean,
        "pstvdev": pstdev,
        # Media armónica: Se usa para promediar tasas o razones (velocidades, precios por unidad...)
        # Da más peso a los valores más pequeños y es menos sensible a los datos atípicos muy elevados,
        # en comparación con la media aritmética.
        "harmonic_mean": statistics.harmonic_mean(nums),
        # 
        "geometric_mean": statistics.geometric_mean(nums),
        "cv": pstdev/mean
    }

if __name__ == "__main__":

    nums = [2, 5, 7, 8, 5, 1, 5, 8, 3]

    print(compare_means(nums))

    try:
        # compare_means([])
        compare_means([0, -1, 2, 3])
    except ValueError as e:
        print("Error tipo: ", e)
