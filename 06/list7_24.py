import numpy as np

arr = np.array([4, -9, 16, -4, 20])
print(arr)

# 変数arrの各要素を絶対値にし、変数arr_absに代入してください。
arr_abs = np.abs(arr)
print(arr_abs)

# 変数arr_absの各要素のeのべき乗と平方根を出力してください。
print(np.exp(arr_abs))
print(np.sqrt(arr_abs))
