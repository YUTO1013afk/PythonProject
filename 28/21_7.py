# 吉村の環境では、以下の2行でエラーのため動作せず。
from keras.datasets import mnist
from keras.layers import Activation,Conv2D,Dense,Flatten,MaxPooling2D
from keras.layers import Activation, Dense, Dropout
from keras.utils.vis_utils import plot_model
from keras.models import Sequential, load_model
import numpy as np
import matplotlib.pyplot as plt
# 以下のように変更した。
# from tensorflow.keras.layers import Activation,Conv2D,Dense,Flatten,MaxPooling2D
# from tensorflow.keras.models import Sequential, load_model
from keras.utils.np_utils import to_categorical
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# データをロードします
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 学習には300枚、テストには100枚のデータを使用します
# Convレイヤーは４次元配列を受け取ります(バッチサイズ×縦×横×チャンネル数)
# MNISTのデータを４次元に変換する
X_train = X_train[:300].reshape(-1, 28, 28, 1)
X_test = X_test[:100].reshape(-1, 28, 28, 1)
y_train = to_categorical(y_train)[:300]
y_test = to_categorical(y_test)[:100]

# モデルを定義します
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3),input_shape=(28,28,1)))
model.add(Activation("relu"))
model.add(Conv2D(filters=64, kernel_size=(3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(10))
model.compile(optimizer='adadelta', loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, batch_size=128, epochs=1, verbose=1, validation_data=(X_test, y_test))

# 制度を評価します
score = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# データを可視化します(テストデータの先頭の10枚)
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[i].reshape(28,28), 'gray')
plt.suptitle("The first ten of the test data",fontsize=20)
plt.show()

# 予測します(テストデータの先頭の10枚)
pred = np.argmax(model.predict(X_test[0:10]), axis=1)
print(pred)

model.summary()