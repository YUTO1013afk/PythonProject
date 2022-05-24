import numpy as np

arr = np.arange(16).reshape(4,4)*10
# print(arr)

# 2行目の合計を求める
# print(arr.sum(axis=1))
print(arr.sum(axis=1)[2])


# 2列目の合計を求める
# print(arr.sum(axis=0))
print(arr.sum(axis=0)[2])


# 0行目の最大値を求める
# print(arr.max(axis=1))
print(arr.max(axis=1)[0])


# 3列目の最大値を求める
# print(arr.max(axis=0))
print(arr.max(axis=0)[3])
