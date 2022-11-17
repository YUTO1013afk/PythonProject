from dtreeviz.trees import dtreeviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn import tree
X, y = make_classification(
n_samples=100, n_features=2, n_redundant=0, random_state=42)
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=42)
model = DecisionTreeClassifier()
model.fit(train_X, train_y) # 学習用データでモデルを訓練・適合(fit)
model.predict(test_X) # 評価用データに対するモデルの予測(predict)結果
print('正解率は{}'.format(model.score(test_X, test_y)))
print(tree.plot_tree(model))
viz = dtreeviz(model, train_X, train_y, target_name='dtreeviz test')
viz.save('dtreeviz_test.svg')
# viz.view()