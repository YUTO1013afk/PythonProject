from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
# zip()にて複数リストの値を同時に取得しています。
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:10]):
    plt.subplot(2, 5, index + 1)
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('digit:%i' % label)
plt.show()