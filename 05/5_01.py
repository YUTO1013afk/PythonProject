import numpy as np

# Python 標準の range()関数は,開始・終了・増分に「整数」のみ指定可能
nums1 = range(0, 10, 1)
array1 = list(nums1)
print(type(array1))
print(array1)

print()	#見やすさのため空改行

# NumPy の arange()メソッドは,開始・終了・増分に「小数」が指定可能
nums2 = np.arange(0.0, 1.0, 0.1)
# np.array()メソッドによって生成された ndarray オブジェクト
array2 = np.array(nums2)
print(type(array2))
print(array2)