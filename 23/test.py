import time
import scipy.stats
from sklearn.datasets import load_breast_cancer
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

#乳癌データの読み込み
cancer_data = load_breast_cancer()

#条件設定
max_score = 0
SearchMethod = 0
LSVC_grid = {LinearSVC(): {"C": [10 ** i for i in range(-5, 6)],
"multi_class": ["ovr", "crammer_singer"],
"class_weight": ["balanced"],
"random_state": [i for i in range(0, 101)]}}
LSVC_random = {LinearSVC(): {"C": scipy.stats.uniform(0.00001, 1000),
"multi_class": ["ovr", "crammer_singer"],
"class_weight": ["balanced"],
"random_state": scipy.stats.randint(0, 100)}}

#トレーニングデータ、テストデータの分離
train_X, test_X, train_y, test_y = train_test_split(cancer_data.data, cancer_data.target, random_state=0)

#グリッドサーチ
for model, param in LSVC_grid.items():
    clf = GridSearchCV(model, param, n_jobs=-1)
    clf.fit(train_X, train_y)
    pred_y = clf.predict(test_X)
    score = f1_score(test_y, pred_y, average="micro")

    if max_score < score:
        max_score = score
        best_param = clf.best_params_
        best_model = model.__class__.__name__

#ランダムサーチ
for model, param in LSVC_random.items():
    clf =RandomizedSearchCV(model, param, n_jobs=-1)
    clf.fit(train_X, train_y)
    pred_y = clf.predict(test_X)
    score = f1_score(test_y, pred_y, average="micro")

    if max_score < score:
        SearchMethod = 1
        max_score = score
        best_param = clf.best_params_
        best_model = model.__class__.__name__

if SearchMethod == 0:
    print("サーチ方法:グリッドサーチ")
else:
    print("サーチ方法:ランダムサーチ")
print("ベストスコア:{}".format(max_score))
print("モデル:{}".format(best_model))
print("パラメーター:{}".format(best_param))

#ハイパーパラメータを調整しない場合との比較
model = LinearSVC()
model.fit(train_X, train_y)
score = model.score(test_X, test_y)
print("")
print("デフォルトスコア:", score)