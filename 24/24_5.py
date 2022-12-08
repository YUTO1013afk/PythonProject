import cv2
from sklearn.datasets import fetch_openml
import pickle
import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

CLFFILENAME = './clf.pkl'
IMGFILENAME = "./500x500.png"

if(os.path.exists(CLFFILENAME)):
    with open(CLFFILENAME, 'rb') as f:
        clf = pickle.load(f)

else:
    # MNISTのデータ取得
    mnist = fetch_openml('mnist_784', version=1, data_home='./scikit_learn_data')

    # 属性を表示・確認
    print(mnist.keys())

    images = mnist.data.to_numpy()
    labels = mnist.target

    # 画像の件数は７万個。画像の大きさは 28×28=784 pixel
    print("画像データ数：", images.shape)
    print("ラベルデータ数：", labels.shape)

    train_imgs, test_imgs, train_lbls, test_lbls = \
        train_test_split(images, labels, test_size=1000, train_size=5000, stratify=labels)

    # サポートベクターマシンを利用
    clf = SVC()
    clf.fit(train_imgs, train_lbls)

    print(clf.score(test_imgs, test_lbls))

    with open(CLFFILENAME, "wb") as f:
        pickle.dump(clf, f)


# 画像ファイルの読み込み
img_bgr = cv2.imread(IMGFILENAME)

# グレースケールに変換
img_gry = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 28×28 にリサイズ
img_28 = cv2.resize(img_gry, dsize=(28, 28), interpolation=cv2.INTER_LANCZOS4)

# 白:255 黒:0 なので、反転させる
img = 255 - img_28

# とりあえず、人間に分かるように表示
for yy in range(0, len(img)):
    for xx in range(0, len(img[yy])):
        print("{:3}".format(img[yy][xx]), end='')
    print()

# 1次元配列に変換して、予測
predic_num = clf.predict(img.reshape(-1, 784))

print("認識結果=", predic_num[0])