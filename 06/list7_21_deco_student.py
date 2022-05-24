import numpy as np
import time


def run_time(func):
    '''startとendを前後に出⼒するデコレータ'''
    def funcname(*args, **kwargs):
        start = time.time()
        reslut = func(*args, **kwargs)
        print(f'関数 {func.__name__} の実行時間 {float(time.time()-start):.3f}[sec]')
        return reslut
    return funcname


# 実行時間が短すぎるので、大きな要素で実行
loop = 1500

arr = np.arange(loop)


# pythonのListを使った方法
@run_time
def python_do():
    for _ in range(loop):
        result_arr = []
        for i in range(arr):
            if i % 2 == 0:
                result_arr.append(i)
    return result_arr


# Listの内包表記を使った方法
@run_time
def py_arr_do():
    for _ in range(loop):
        result_arr = [n for n in arr if n % 2 == 0]
    return result_arr


# lambdaとfilterを使った方法
@run_time
def lambda_do():
    for _ in range(loop):
            result_arr = list(filter(lambda n: n % 2 == 0, arr))
    return result_arr


# NumPyの配列を使った方法
@run_time
def numpy_do():
    for _ in range(loop):
        result_arr = arr[arr % 2 == 0]
    return result_arr


# main
python_do()
py_arr_do()
lambda_do()
numpy_do()
