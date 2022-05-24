import numpy as np

arr = np.array([
    [0, 1, 2, 3, 4],
    [-10, -11, -12, -13, -14],
    [20, 21, 22, 23, 24],
])

print(arr.sum())    # または print(np.sum(arr))
print(arr.mean())   # または print(np.mean(arr)) print(np.average(arr))
print(arr.max())    # または print(np.max(arr)) print(np.amax(arr))
print(arr.min())    # または print(np.min(arr)) print(np.amin(arr))
print(arr.argmax())  # または print(np.argmax(arr))
print(arr.argmin())  # または print(np.argmin(arr))
print(np.abs(arr))  # または print(np.absolute(arr))
print(np.sqrt(np.abs(arr)))
