import numpy as np
print(np.full((2, 3, 4), -1))

print(np.array([-1] * 24).reshape(2, 3, 4))
print('-' * 40)

print(np.zeros((2, 3, 4)) - 1)
# print(np.zeros((2, 3, 4), dtype=np.int64) - 1)
print('-' * 40)
