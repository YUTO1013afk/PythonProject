import numpy as np
data = np.random.randint(0, 100, 100)
odd = list(filter(lambda x: x % 2 == 1, data))
print(odd)