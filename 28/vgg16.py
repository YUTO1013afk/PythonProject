from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.applications.vgg16 import decode_predictions
import numpy as np
import keras

img_path = 'apple.jpg'

img = keras.utils.load_img(img_path, target_size=(224, 224))
img = keras.utils.img_to_array(img)
img = np.expand_dims(img, axis=0)
img = preprocess_input(img)

model = VGG16(weights="imagenet")
model.summary()

preds = model.predict(img)
result = decode_predictions(preds, top=5)[0]
print(result)
for _ , name , score in result:
    print('{}: {:.2%}'.format(name, score))