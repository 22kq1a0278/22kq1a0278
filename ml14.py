import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.insert(a, 2, 100)
print("After insertion:", b)
c = np.delete(b, 4)
print("After deletion:", c)