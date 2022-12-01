import time
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

data = load_digits()
train_X, test_X, train_y, test_y = train_test_split(
data.data, data.target, random_state=42)

# ⾮線形 SVM（パラメタはすべて既定値）で学習‧検証する
# clf は クラス分類器(classifier)を指す 慣⽤的な略語
clf = SVC()
clf.fit(train_X, train_y)

# 正解率を出⼒する２つの書き⽅。どちらも同じ結果
print(clf.score(test_X, test_y))

# パラメタの候補値をリストで与える
models = SVC()
params = {
"kernel": ["linear", "poly", "rbf", "sigmoid"],
"C": [10 ** i for i in range(-5, 5)],
"decision_function_shape": ["ovr", "ovo"],
"random_state": [0, 10, 20, 30, 40]
}

# グリッドサーチ（総当たり）で最適パラメタを探す
print("グリッドサーチ開始")
start_time = time.perf_counter()
clf = GridSearchCV(models, params)
clf.fit(train_X, train_y)

print("グリッドサーチ終了")
print("経過時間(秒):{}".format(time.perf_counter() - start_time))
print("最良のスコア：{}".format(clf.best_score_))
print("最良パラメタ：{}".format(clf.best_params_))
print("最良の評価器：{}".format(clf.best_estimator_))
print(clf.score(test_X, test_y))