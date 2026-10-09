# Deduplicar conservando el orden de aparición original. Es
# decir, elimina las copias repetidas de una lista.

original = [1, 5, 7, 3, 10, 0, 5, 1, 1]

deduplicado = list(dict.fromkeys(original))

print(original)
print(deduplicado)