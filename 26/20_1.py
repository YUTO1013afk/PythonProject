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

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

model = Sequential()
model.add(Dense(256, input_dim=784))
# ハイパーパラメータ：活性化関数
model.add(Activation("sigmoid"))
# ハイパーパラメータ：隠れ層の数、隠れ層のチャンネル数
model.add(Dense(128))
model.add(Activation("sigmoid"))
# ハイパーパラメータ：ドロップアウトする割合（rate）
model.add(Dropout(rate=0.5))
model.add(Dense(10))
model.add(Activation("softmax"))

# ハイパーパラメータ：学習率（lr）
sgd = optimizers.SGD(lr=0.01)

# ハイパーパラメータ：最適化関数（optimizer）
# ハイパーパラメータ：誤差関数（loss）
model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

# ハイパーパラメータ：バッチサイズ（batch_size）
# ハイパーパラメータ：エポック数（epochs）
model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1)

score = model.evaluate(X_test, y_test, verbose=0)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))