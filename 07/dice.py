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
    result = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # 試行
    for _ in range(loop_count):
        dice = np.random.randint(1, 7)
        result[dice] += 1
    return result

# main


N = 10000   # 振る回数
for k, v in n_dice(N).items():
    print(f'{k} - {(v/N):.04f}\t', end='')
