import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# データを生成します
X, y = make_classification(n_samples=100, n_features=2,
                           n_redundant=0, random_state=42)
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=42)

# パラメータCを幾つか試す
c_list = [10 ** i for i in range(-5, 5)]

train_accuracy = []
test_accuracy = []

for c in c_list:
    model = LogisticRegression(C=c, random_state=42)
    model.fit(train_X, train_y)

    train_accuracy.append(model.score(train_X, train_y))
    test_accuracy.append(model.score(test_X, test_y))


# グラフのスケールを調整します
plt.semilogx(c_list, train_accuracy, label='accuracy of train_data')
plt.semilogx(c_list, test_accuracy, label='accuracy of test_data')
plt.title('accuracy by changing C')
plt.xlabel('C')
plt.ylabel('accuracy')
plt.legend()
plt.grid(True)
plt.show()
