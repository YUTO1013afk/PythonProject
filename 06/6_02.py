import numpy as np


arr = np.array([
    [0, 1, 2, 3, 4],
    [-10, -11, -12, -13, -14],
    [20, 21, 22, 23, 24],
])

print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)

arr = np.array([
    [0.0, 1, 2, 3, 4],
    [-10, -11, -12, -13, -14],
    [20, 21, 22, 23, 24],
])

print(arr)
print(arr.dtype)

arr = np.array([
    [0, 1, 2, 3, 4],
    [-10, -11, -12, -13, -14],
    [20, 21, 22, 23, 24],
], dtype=float)

print(arr)
print(arr.dtype)
