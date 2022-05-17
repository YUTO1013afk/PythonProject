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


# 行、列の大きさ
N = 150

storages = np.arange(N)

# 1回の処理では速すぎて分からないので、同じ処理を多数繰り返す
loop = 3000


# テキスト P.178の方法
@run_time
def python_do():
    for _ in range(loop):
        new_storages = []
        for n in storages:
            n += n
            new_storages.append(n)
    return new_storages


# Listの内包表記を使った例
@run_time
def py_arr_do():
    for _ in range(loop):
        new_storages = [n + n for n in range(loop)]
    return new_storages


# Lambdaを使用した例
@run_time
def py_map_do():
    for _ in range(loop):
        new_storages = list(map(lambda n: n + n, storages))
    return new_storages


# nampyの配列同士の足し算
@run_time
def numpy_do():
    for _ in range(loop):
        new_storages = storages + storages
    return new_storages


python_do()
py_arr_do()
py_map_do()
numpy_do()