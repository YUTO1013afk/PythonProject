import pandas as pd

# P.221 リスト8.1
fruits1 = {"orange": 2, "banana": 3}
print(pd.Series(fruits1))
print()

# P.227 リスト8.8
fruits2 = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}
series2 = pd.Series(fruits2)
print(series2[0:2])
print()

# P.227 リスト8.9
print(series2[["orange", "peach"]])

# P.229 series.valuesとするとデータの値
# P.229 series.indexとするとインデックスの参照

# P.230 series.append()に渡して要素を追加できる

# P.232 series.drop("インデックス")で削除することができる

# P.233 Series型において条件に一致する要素を取り出したい場合に、series[ ][ ]のように[ ]を複数組後ろに付け加える

# P.235 インデックスのソートはseries.sort_index()
# P.235 データのソートはseries.sort_values()
