import numpy as np
import time
from numpy.random import rand

# 行、列の大きさ
N = 150

# 行列の初期化
matA = np.array(rand(N, N))
matB = np.array(rand(N, N))
matC = np.array([[0.0]*N for _ in range(N)])

# Python

# 開始時刻の取得
start = time.time()

# for
for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] += matA[i][k] * matB[k][j]
print(matC)

print("Pythonの機能のみでの計算結果:%.3f[sec]" % float(time.time()-start))

# numpy

start = time.time()

# numpyの行列計算
matC = np.dot(matA, matB)
print(matC)

print("Numpy を使った場合の計算結果:%.3f[sec]" % float(time.time()-start))
