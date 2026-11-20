import numpy as np
a = np.array([10, -5, 0, 20, -8, 0])
print("Positive:", np.sum(a > 0))
print("Negative:", np.sum(a < 0))
print("Zeros:", np.sum(a == 0))
