import numpy as np
import time
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential, load_model
from keras import optimizers
from keras.utils.np_utils import to_categorical
# WARNING抑制
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# OMP Errorが出る場合
# import os
# os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Ubuntu22.04上での実行時に以下のエラーが発生する
# libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: 共有オブジェクトファイルを開けません: そのようなファイルやディレクトリはありません (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
#
# 回避策：GPUの設定を変更
# https://bugs.launchpad.net/ubuntu/+source/matlab-support/+bug/1872277
# export MESA_LOADER_DRIVER_OVERRIDE=i965

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 784)[:60000]
X_test = X_test.reshape(X_test.shape[0], 784)[:10000]
y_train = to_categorical(y_train)[:60000]
y_test = to_categorical(y_test)[:10000]

model = Sequential()
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))
def funcA():
    model.add(Dense(128))
    model.add(Activation("sigmoid"))

def funcB():
    model.add(Dense(128))
    model.add(Activation("sigmoid"))
    model.add(Dense(128))
    model.add(Activation("sigmoid"))
    model.add(Dense(128))
    model.add(Activation("sigmoid"))

def funcC():
    model.add(Dense(1568))
    model.add(Activation("sigmoid"))

start = time.time()
funcA() #30秒くらい
funcB() #32秒くらい
funcC() #70秒くらい

model.add(Dropout(rate=0.5))
model.add(Dense(10))
model.add(Activation("softmax"))

sgd = optimizers.SGD(lr=0.1)
model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

# epochs数は3を指定します
history = model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1)

score = model.evaluate(X_test, y_test, verbose=0)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))
t = time.time() - start
print(f'時間差：{t}')

# epochs=3 約82秒 loss 2.3 acc 0.1 
# epochs=5 約150秒 loss 2.3 acc 0.1
# epochs=10 約215秒 loss2.3 acc 0.1