import numpy as np

def mostrar_tamanyo(array: np.array):

    for i, tamanyo in enumerate(array.shape):
        print(f"El numero de elementos de la dimension {i} es {tamanyo}.")


ejemplo = np.array([ [ [2, 3], [5, 7]], [ [11, 13], [17, 19]], [ [23, 29], [31, 37] ] ] )
mostrar_tamanyo(ejemplo)
print()

a = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
mostrar_tamanyo(a)
print()

b = np.array([[2, 3], [5, 7], [11, 13], [17, 19], [23, 29], [31, 37]])
mostrar_tamanyo(b)
print()
c = np.array([[[2, 3], [5, 7]], [[11, 13], [17, 19]], [[23, 29], [31, 37]]])
mostrar_tamanyo(c)