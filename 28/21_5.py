# 吉村の環境では、以下の2行でエラーのため動作せず。
from keras.layers import Activation,Conv2D,Dense,Flatten,MaxPooling2D
from keras.models import Sequential, load_model
# 以下のように変更した。
# from tensorflow.keras.layers import Activation,Conv2D,Dense,Flatten,MaxPooling2D
# from tensorflow.keras.models import Sequential, load_model
from keras.utils.np_utils import to_categorical

# モデルを定義します
model = Sequential()
# --------------------------------------------------------------
# ここにコードを記述してください
model.add(Conv2D(input_shape=(28, 28, 1),
                 filters=32,
                 kernel_size=(2, 2),
                 strides=(1, 1),
                 padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2),
                       strides=(1, 1)))
model.add(Conv2D(filters=32,
                 kernel_size=(2, 2),
                 strides=(1, 1),
                 padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2),
                       strides=(1, 1)))
# --------------------------------------------------------------

model.add(Flatten())
model.add(Dense(256))
model.add(Activation('sigmoid'))
model.add(Dense(128))
model.add(Activation('sigmoid'))
model.add(Dense(10))
model.add(Activation('softmax'))

model.summary()
