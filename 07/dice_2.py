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


@run_time
def n_dice(loop_count):
    # 結果格納用result初期化
    result = {}
    for i in range(1, dice_N + 1):
        result[i] = 0

    # 試行
    for _ in range(loop_count):
        dice = np.random.randint(1, dice_N + 1)
        result[dice] += 1
    return result

# main


dice_N = 7  # diceの面数
try_N = [100, 1000, 10000, 100000]   # 振る回数
for N in try_N:
    for k, v in n_dice(N).items():
        print(f'{k} - {(v/N):.04f}\t', end='')
    print(f'試行回数:{N}')
