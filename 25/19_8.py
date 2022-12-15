from keras.datasets import mnist
import os
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils.vis_utils import plot_model
from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt
# ライブラリの重複を検出しても処理を進めるというもの
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

model = Sequential()
# 入力ユニット数は 784、1つ目の全結合層の出力ユニット数は 256 です
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))

# 2つ目の全結合層の出力ユニット数は 128 です
# ---------------------------
# ここにコードを記述してください
model.add(Dense(128))
model.add(Activation("sigmoid"))
# ---------------------------

# 3つ目の全結合層（出力層）の出力ユニット数は 10 です
model.add(Dense(10))
model.add(Activation("softmax"))

model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

# epochs数は5を指定します。
history = model.fit(X_train, y_train, verbose=1, epochs=5)

# accuracy、val_accuracyのプロットです
plt.plot(history.history["accuracy"], label="acc", ls="-", marker="o")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(loc="best")
plt.show()