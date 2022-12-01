import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()

# cmap=plt.cm.gray_r 	白黒で表現する。
# interpolation=nearest 最近傍補間という補完を行なっている
# 最近傍補間			  拡大・縮小・回転した際に利用する補間法
# plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')

# plt.axis('off')
plt.show()