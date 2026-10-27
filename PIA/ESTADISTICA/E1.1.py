# Ejercicio 1: resumen de cinco números (mínimo, Q1, mediana, Q3, máximo)
# usando statistics.quantiles y statistics.median.

import statistics


def five_number_summary(nums):
    """Devuelve (min, Q1, mediana, Q3, max) de una lista de números."""
    if not nums:
        raise ValueError("La lista no puede estar vacía.")

    # Con un solo dato no se pueden calcular cuartiles: todo coincide.
    if len(nums) == 1:
        return nums[0], nums[0], nums[0], nums[0], nums[0]

    cuartiles = statistics.quantiles(nums, n=4)
    return min(nums), cuartiles[0], statistics.median(nums), cuartiles[2], max(nums)


def main():
    nums = [12, 7, 3, 15, 8, 22, 5, 9, 14, 10]
    minimo, q1, mediana, q3, maximo = five_number_summary(nums)
    print(f"Datos: {sorted(nums)}")
    print(f"Mínimo: {minimo}")
    print(f"Q1:     {q1}")
    print(f"Mediana:{mediana}")
    print(f"Q3:     {q3}")
    print(f"Máximo: {maximo}")


if __name__ == "__main__":
    main()
