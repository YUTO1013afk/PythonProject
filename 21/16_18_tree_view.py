from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn import tree
import graphviz

# P.514 二項分類用データ生成
X, y = make_classification(
    n_samples=100, n_features=2, n_redundant=0, random_state=42)


# P.518 学習用と評価用にデータを分割
train_X, test_X, train_y, test_y = \
    train_test_split(X, y, random_state=42)

# modelを指定
model = DecisionTreeClassifier()
# 以下でも良い
# model = tree.DecisionTreeClassifier()
model.fit(train_X, train_y)  # 学習用データでモデルを訓練・適合(fit)
model.predict(test_X)        # 評価用データに対するモデルの予測(predict)結果
print('正解率は{}'.format(model.score(test_X, test_y)))

print(tree.plot_tree(model))

dot_data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(dot_data)
# format指定をしないとpdf
graph.render("tree", format='png')
