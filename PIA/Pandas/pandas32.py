import pandas as pd

# Verificar con equals si dos series contienen los mismos elementos
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([1, 2, 3])
s3 = pd.Series([3, 2, 1])

# equals compara valores, índice y tipo
print(s1.equals(s2))   # True
print(s1.equals(s3))   # False
