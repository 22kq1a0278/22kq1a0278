import numpy as np
a = np.array([10, -5, 20, -8, 30])
a[a < 0] = 0
print(a)

