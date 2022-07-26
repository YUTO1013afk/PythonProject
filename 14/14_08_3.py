import numpy as np
data = np.random.randint(0, 100, 100)
x = [i for i in data if i % 2 == 1]
print(x)