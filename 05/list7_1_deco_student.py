import numpy as np
import time
from numpy.random import rand


def run_time(func):
    '''startとendを前後に出⼒するデコレータ'''
    def funcname(*args, **kwargs):
        start = time.time()
        reslut = func(*args, **kwargs)
        print(f'関数 {func.__name__} の実行時間 {float(time.time()-start):.3f}[sec]')
        return reslut
    return funcname


# 行、列の大きさ
N = 150

# 行列の初期化
matA = np.array(rand(N, N))
matB = np.array(rand(N, N))
matC = np.array([[0.0]*N for _ in range(N)])
# matC = np.array([[0]*N for _ in range(N)], dtype=float)

# Python
@run_time
def python_do():
    # for
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matC[i][j] += matA[i][k] * matB[k][j]
    print(matC)


# NumPy
@run_time
def numpy_do():
    # numpyの行列計算
    matC = np.dot(matA, matB)
    print(matC)


# main
python_do()
numpy_do()