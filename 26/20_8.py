import numpy as np
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

X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

model = Sequential()
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))
model.add(Dense(128))
model.add(Activation("sigmoid"))
model.add(Dropout(rate=0.5))
model.add(Dense(10))
model.add(Activation("softmax"))

sgd = optimizers.SGD(lr=0.1)
model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

def  funcA():
    global batch_size
    batch_size = 16

def funcB():
    global batch_size
    batch_size = 32

def funcC():
    global batch_size
    batch_size = 64

# batch_size: 16
funcA() # accuracy: 0.6477
# batch_size: 32
funcB() # accuracy: 0.7238
# batch_size: 64
funcC() # accuracy: 0.7240

# funcA(), B(), C() accuracy: 0.7365

model.fit(X_train, y_train, batch_size=batch_size, epochs=3, verbose=1)
score = model.evaluate(X_test, y_test, verbose=0)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))