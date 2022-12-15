import numpy as np
import os
from keras.datasets import mnist
from keras.layers import Activation, Dense
from keras.models import Sequential
from keras import optimizers
from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt
# ライブラリーの重複を検出しても処理を進めるというもの
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]

y_test_orig = y_test[0:10]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

model = Sequential()
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))
model.add(Dense(128))
model.add(Activation("sigmoid"))
model.add(Dense(10))
model.add(Activation("softmax"))

model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, epochs=11, verbose=1)

score = model.evaluate(X_test, y_test, verbose=0)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

# 予測結果を表示する
pred = np.argmax(model.predict(X_test[0:10]), axis=1)
print("予測結果",pred)

# 実際の結果を表示する
print("実際の値",y_test_orig)

# テストデータの最初の10枚を表示する
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_test[i].reshape(28, 28), "gray")
plt.show()