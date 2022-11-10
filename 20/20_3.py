from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()


train_X, test_X, train_y, test_y = \
    train_test_split(iris.data, iris.target,
    stratify=iris.target, random_state=42)

model = KNeighborsClassifier()
model.fit(train_X, train_y)  # 学習用データでモデルを訓練・適合(fit)
model.predict(test_X)        # 評価用データに対するモデルの予測(predict)結果
print('正解率は{}'.format(model.score(test_X, test_y)))
