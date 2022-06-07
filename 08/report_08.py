import pandas as pd

# データ(csv)のロード
titanic_df = pd.read_csv("titanic.csv")
titanic_df

# データのサイズ
titanic_df.shape[0]

# データのカラム
# データのカラムは DataFrame.columnsで見ることが出来る。
titanic_df.columns

# ⾏列から必要な列(カラム)を取り出す
# 1列を取り出す： [] でキーを指定 Series型が返ってくる
titanic_df['Age']

# 2列以上を取り出す: []にキーの配列を指定 DataFrame型で帰ってくる
titanic_df[['Age', 'Sex']]

# こんな風にして必要なキーだけを宣言し、絞り込むような事が多い。
valiables = ['Survived', 'Pclass', 'Sex', 'Age']
titanic_df = titanic_df[valiables]
titanic_df

# 条件にマッチするデータを取り出す
# 1つの条件にマッチするデータを取り出す
titanic_df.query('Age > 20')

# 2つ以上の条件にマッチするデータを取り出す
titanic_df.query('(Age > 20) & (Sex == "female")')

# True/FalseのSeries型を指定し、Trueの行だけを取り出す
titanic_df['Age'] > 20

# このTrue/FalseのSeriesを更にDataFrameに指定することで、Trueの行だけを取り出すことができる
titanic_df[titanic_df['Age'] > 20]

# 複数条件を並べる場合は()で条件同士はくくってあげる必要がある。
titanic_df[(titanic_df['Age'] > 20) & (titanic_df['Sex'] == 'female')]

# 行列から必要な行番号を指定してを取り出す
# 行を取り出すには、DataFrame.locという関数を使っていく。
# DataFrame.loc[start:end]としたときに、startとendをどちらも含んだ状態で取り出す
titanic_df.loc[0:2]

# グループ分けと集計
# Survive列が0か1かで生存したかどうかを示している。
# 生存した人たちと、していない人たちで各値の平均をとってみる。
titanic_df.groupby(['Survived']).mean()

# reset_index()を呼び出すことでこの行列自体を更に操作していきやすくなる。
titanic_df.groupby(['Survived']).mean().reset_index()

# 新たな列を追加する
# 固有値を追加する
titanic_df.assign(
    One = 1
)

# 他の列を加工して新たな列を作る
titanic_df.assign(
    IsChild = titanic_df['Age'] < 20
)

# True=1, False=0 にして入れる場合
titanic_df.assign(
    IsChild = (titanic_df['Age'] < 20).astype(int)
)

titanic_df['IsChild'] = (titanic_df['Age'] < 20).astype(int)
titanic_df

# 他の複数列を加工して新たな列を作る
# Pclassの値とSurvivedの値を足した列
titanic_df.apply(lambda x: x['Pclass'] + x['Survived'], axis=1)

titanic_df.assign(
    X=titanic_df.apply(lambda x: x['Pclass'] + x['Survived'], axis=1)
)

# 処理速度が早いVer
titanic_df.assign(
    X=titanic_df['Pclass'] + titanic_df['Survived']
)

# 条件にあったセルだけを書き換える
# IsChildの1のところを1ではなく5にしてみる。
titanic_df.loc[titanic_df['IsChild'] == 1, ['IsChild']] = 5
titanic_df

# setやリストに存在する値のデータだけを取り出す
# PClassが1か3の場合の行を取り出したいとする。
# DataFrame.isinを使う
target_set = set([1, 3])

condition = titanic_df['Pclass'].isin(target_set)
print(titanic_df[condition])