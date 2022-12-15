from keras.datasets import mnist
import os
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
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

model = Sequential()
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))
model.add(Dense(128))
model.add(Activation("sigmoid"))
model.add(Dense(10))
model.add(Activation("softmax"))

model.compile(optimizer="sgd", loss="categorical_crossentropy",
              metrics=["accuracy"])
# ---------------------------
# ここにコードを記述してください
history = model.fit(X_train, y_train,epochs=11, validation_data=(X_test, y_test))

# score = model.evaluate(X_test, y_test, verbose=1)
print("evaluate loss: {0}\nevaluate acc: {1}".format(history.history['val_loss'][-1],history.history['val_accuracy'][-1]))
# ---------------------------
# acc、val_accのプロット
plt.plot(history.history["accuracy"], label="acc", ls="-", marker="o")
plt.plot(history.history["val_accuracy"], label="val_acc", ls="-", marker="x")
plt.plot(history.history["loss"], label="loss", ls="-", marker="o")
plt.plot(history.history["val_loss"], label="val_loss", ls="-", marker="x")
plt.ylabel("accuracy / loss")
plt.xlabel("epoch")
plt.legend(loc="best")
plt.grid(True)
plt.show()