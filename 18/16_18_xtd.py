import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from mlxtend.plotting import plot_decision_regions
from sklearn.tree import DecisionTreeClassifier

# P.514 二項分類用データ生成
X, y = make_classification(
    n_samples=100, n_features=2, n_redundant=0, random_state=42)


# P.518 学習用と評価用にデータを分割
train_X, test_X, train_y, test_y = \
    train_test_split(X, y, random_state=42)
# train_test_split(X, y, test_size=0.25, random_state=42)

# 決定木で学習
model = DecisionTreeClassifier()
model.fit(train_X, train_y)  # 学習用データでモデルを訓練・適合(fit)
model.predict(test_X)        # 評価用データに対するモデルの予測(predict)結果
print('正解率は{}'.format(model.score(test_X, test_y)))

# 元々のplt.scatter( ) はコメント
# p.521 散布図を描く
# 学習用データは'.'印で，評価用データは'x'印でプロット
# plt.scatter(train_X[:, 0], train_X[:, 1], c=train_y, marker='.',
#             cmap=matplotlib.cm.get_cmap(name='bwr'), alpha=0.7)
# plt.scatter(test_X[:, 0], test_X[:, 1], c=test_y, marker='*',
# cmap=matplotlib.cm.get_cmap(name='bwr'), alpha=0.7)


# 学習して導出した識別境界線をプロット
# 学習後のモデル内には二項を分類する境界直線の属性値が求まった
# w0 = model.intercept_
# w1 = model.coef_[0][0]
# w2 = model.coef_[0][1]

# モデル内の属性値は境界直線の式を表す
#  w0 + (w1 * x) + (w2 * y) = 0
# 変形すると
#  y = -(w1 / w2) * x - (w0 / w2)
# つまり，
#  傾きが -(w1 / w2)
#  切片が -(w0 / w2)
# Xi = np.linspace(-10, 10, 20)
# Y = -(w1 / w2) * Xi - (w0 / w2)
# plt.plot(Xi, Y)

# グラフのスケールを調整
plt.xlim(min(X[:, 0]) - 0.5, max(X[:, 0]) + 0.5)
plt.ylim(min(X[:, 1]) - 0.5, max(X[:, 1]) + 0.5)
# 別の書き方
# plt.axis([min(X[:, 0]) - 0.5, max(X[:, 0]) + 0.5,
#           min(X[:, 1]) - 0.5, max(X[:, 1]) + 0.5])

# タテヨコ比を 1 対 1 にする
plt.gca().set_aspect('equal', 'datalim')
# plt.axes().set_aspect('equal', 'datalim')
# *** この指定では、Warningが発生 ***
# MatplotlibDeprecationWarning:  Adding an axes using the same arguments
# as a previous axes currently reuses the earlier instance. In a future
# version, a new instance will always be created and returned.
#   Meanwhile, this warning can be suppressed, and the future behavior
# ensured, by passing a unique label to each axes instance.
#
# https://stackoverflow.com/questions/47953061/matplotlib-axes-collision-warning-when-setting-aspect-ratio
#

plt.grid(True)
plt.title("classification data using DecisionTreeClassifier")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# 最後の表示前に以下を追加
output_X = np.concatenate([train_X, test_X])	# 出力用の全データ 学習用＋評価用 の順
output_y = np.concatenate([train_y, test_y])	# 出力用の全データ 学習用＋評価用 の順
scatter_kwargs = {'s': 100, 'edgecolor': None, 'alpha': 0.7}	# 散布図用表示設定
scatter_highlight_kwargs = {'s': 100, 'label': 'Test data', 'alpha': 0.7}	# 評価用表示設定
plot_decision_regions(output_X, output_y, model, legend=1, X_highlight=test_X, scatter_kwargs=scatter_kwargs, scatter_highlight_kwargs=scatter_highlight_kwargs)
plt.show()