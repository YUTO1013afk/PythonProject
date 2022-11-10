from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
mush_data = pd.read_csv('agaricus-lepiota.data', header=None)
# make_columns.pyの結果を利⽤する
mush_data.columns = ['classes', 'cap-shape', 'cap-surface', 'cap-color',
'bruises?', 'odor', 'gill-attachment', 'gill-spacing',
'gill-size', 'gill-color', 'stalk-shape', 'stalk-root',
'stalk-surface-above-ring', 'stalk-surface-below-ring',
'stalk-color-above-ring', 'stalk-color-below-ring',
'veil-type', 'veil-color', 'ring-number', 'ring-type',
'spore-print-color', 'population', 'habitat']
# この時点で、mush_dataがどうなっているか、確認する
# print(mush_data) # (A)
# exit()
# pd.get_dummies() 処理の前に値を確認する。処理後再度確認する。
# どう変化したか？ BとCで⽐較
# print(mush_data[['gill-size', 'gill-attachment', 'odor', 'cap-color']]) # (B)
# exit()
mush_data_dummy = pd.get_dummies(
mush_data[['gill-size', 'gill-attachment', 'odor', 'cap-color']])
# print(mush_data_dummy) # (C)
# exit()
mush_data_dummy['flg'] = mush_data['classes'].map(
lambda x: 1 if x == 'p' else 0)
# mush_data_dummy はどうなったか？ CとDで⽐較
# print(mush_data_dummy) # (D)
# exit()
# この2⾏は何を⾏なっているのか？
X = mush_data_dummy.drop("flg", axis=1)
Y = mush_data_dummy["flg"]
train_X, test_X, train_y, test_y = train_test_split(X, Y, random_state=42)
model = DecisionTreeClassifier()
model.fit(train_X, train_y)
model.predict(test_X)
print('正解率は{}'.format(model.score(test_X, test_y)))