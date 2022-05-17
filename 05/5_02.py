import numpy as np

# Python 標準のリストの場合
arr_list = [x for x in range(10)]
print(arr_list)
arr_list_copy = arr_list[:]
arr_list_copy[0] = 111
print(arr_list)

# NumPy の多次元配列 ndarray の場合
arr_NumPy = np.arange((10))
print(arr_NumPy)
arr_NumPy_copy = arr_NumPy[:].copy()
arr_NumPy_copy[0] = 222
print(arr_NumPy)
#.copy()が無いと元の配列が変わってしまう。
arr_NumPy_view = arr_NumPy[:]
arr_NumPy_view[0] = 333
print(arr_NumPy)
