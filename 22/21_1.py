from dtreeviz.trees import dtreeviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
train_X, test_X, train_y, test_y = \
    train_test_split(iris['data'], iris['target'], stratify=iris['target'],
                     test_size=0.25, random_state=0)

depth_list = [i for i in range(1,11)]

for max_depth in depth_list:
    model = DecisionTreeClassifier(max_depth=max_depth,random_state=17)

# model = DecisionTreeClassifier()
model.fit(train_X, train_y)
print(model.score(test_X, test_y))

viz = dtreeviz(model, train_X, train_y, target_name='IRIS',
               feature_names=iris['feature_names'],
               class_names=list(iris['target_names']),
               )
viz.save('22_2_md_{}.svg'.format(max_depth))
