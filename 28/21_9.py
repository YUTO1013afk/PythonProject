import keras
from keras.datasets import cifar10
from keras.layers import Activation, Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential, load_model
from keras.utils.np_utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# データをロードします
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# ここでは全データのうち、学習には300、テストには100個のデータを使用します
X_train = X_train[:300]
X_test = X_test[:100]
y_train = to_categorical(y_train)[:300]
y_test = to_categorical(y_test)[:100]


# モデルを定義します
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# --------------------------------------------------------------
# ここにコードを記述してください
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
# --------------------------------------------------------------
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

# コンパイルします
opt = keras.optimizers.RMSprop(lr=0.0001, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

# 学習させます
model.fit(X_train, y_train, batch_size=32, epochs=1)

# 重みの保存をする場合には以下を使います
model.save_weights('param_cifar10.hdf5')

# 精度を評価します
scores = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# データを可視化します（テストデータの先頭の 10 枚）
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[i])
plt.suptitle("The first ten of the test data", fontsize=20)
plt.show()

# 予測します（テストデータの先頭の 10 枚）
pred = np.argmax(model.predict(X_test[0:10]), axis=1)
print(pred)

model.summary()
