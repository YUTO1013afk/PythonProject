import numpy as np

data = np.random.randint(0, 100, 100)

odd = []
for x in data:
    if x % 2 == 1:
        odd.append(x)

print(odd)
