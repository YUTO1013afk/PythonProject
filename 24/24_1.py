import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml

# NIST 提供の Mixed データセットを結び付け
# images,labels = fetch_openml('mnist_784', version=1,
#                      data_home='./scikit_learn_data',return_X_y=True)
# images = images.to_numpy()

mnist = fetch_openml('mnist_784', version=1, data_home='./scikit_learn_data')

# 属性を表示・確認
print(mnist.keys())

images = mnist.data.to_numpy()
labels = mnist.target

# 画像の件数は７万個。画像の大きさは 28×28=784 pixel
print("画像データ数：", images.shape)
print("ラベルデータ数：", labels.shape)

# ランダムに 10 個，表示する準備（該当するindexを10個生成）
rands = np.random.randint(0, len(images), 10)

# subplotsで10個表示する
fig, axs = plt.subplots(2, 5, tight_layout=True)

num = 0
for yy in range(2):
    for xx in range(5):
        axs[yy, xx].imshow(images[rands[num]].reshape(
            28, 28), cmap=plt.cm.gray_r)
        axs[yy, xx].set_title(f'digit:{labels[rands[num]]}({rands[num]})')
        num += 1

plt.show()
