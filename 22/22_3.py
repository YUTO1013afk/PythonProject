import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# データを作成する
x, y = make_classification(n_samples=1000, n_features=4, n_informative=3, n_redundant=0, random_state=42)
train_X,  test_X, train_y, test_y = train_test_split(x, y, random_state=42)

# max_depthの値の範囲(1から10)
depth_list = [1 for i in range(1, 11)]

# 正解率を格納する空リストを作成
accuracy = []

# max_depthを変えながらモデルを学習
for max_depth in depth_list:
    model = DecisionTreeClassifier(max_depth=max_depth,random_state=17)
    model.fit(train_X, train_y)
    accuracy.append(model.score(test_X, test_y))

# n_estimatorsの値の範囲(1から20)です
n_estimators_list = [i for i in range(1, 21)]

# 正解率を格納する空リストを作成
accuracy = []

# n_estimatorを変えながらモデルを学習
for n_estimators in n_estimators_list:
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(train_X, train_y)
    accuracy.append(model.score(test_X, test_y))

# グラフをプロット
plt.plot(n_estimators_list, accuracy)
plt.title("accuracy by changing max_depth")
plt.xlabel("max_depth")
plt.ylabel("accuracy")
plt.show()