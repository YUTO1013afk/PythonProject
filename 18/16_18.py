from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

# 学習データとテストデータに分けます
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=42)

# モデルを読み込みます
from sklearn.tree import DecisionTreeClassifier

# モデルを構築します
model = DecisionTreeClassifier()
# モデルを学習させます
model.fit(train_X, train_y)

# 正解率を算出します
print(model.score(test_X, test_y))