import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# データを生成します
X, y = make_classification(n_samples=100, n_features=2,
                           n_redundant=0, random_state=42)
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=42)

# 生成したデータをプロットします
plt.scatter(X[:, 0], X[:, 1], c=y, marker="o",
            cmap=matplotlib.cm.get_cmap(name="bwr"), alpha=0.7)

# パラメータCを幾つか試す
c_list = [10 ** i for i in range(-5, 5)]


for c in c_list:
    # モデルを構築してください
    model = LogisticRegression(C=c, random_state=42)

    # train_Xとtrain_yを使ってモデルに学習させてください
    model.fit(train_X, train_y)

    # test_Xに対するモデルの分類予測結果を出してください
    pred_y = model.predict(test_X)

    # 学習して導出した識別境界線をプロットします
    Xi = np.linspace(-10, 10)
    Y = -model.coef_[0][0] / model.coef_[0][1] * \
        Xi - model.intercept_ / model.coef_[0][1]
    plt.plot(Xi, Y, label=str(c))

# グラフのスケールを調整します
plt.xlim(min(X[:, 0]) - 0.5, max(X[:, 0]) + 0.5)
plt.ylim(min(X[:, 1]) - 0.5, max(X[:, 1]) + 0.5)
plt.grid(True)

# グラフにタイトルを設定します
plt.title("classification data using LogisticRegression")
# x 軸、y 軸それぞれに名前を設定します
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
