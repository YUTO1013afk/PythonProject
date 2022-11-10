import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()


train_X, test_X, train_y, test_y = \
    train_test_split(iris.data, iris.target,
    stratify=iris.target, random_state=42)

scores = []
k_range = range(1, 100, 2)

for k in k_range:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(train_X, train_y)
    model.predict(test_X)
    score = model.score(test_X, test_y)
    scores.append(score)
    # print('正解率は{}'.format(score))


plt.plot(k_range, scores)
plt.ylim(0, 1)
plt.xlim(0, 100)
plt.grid(True)
plt.xlabel("n_neighbors")
plt.ylabel("k-NN score")
plt.show()
plt.savefig("Fig.png")
