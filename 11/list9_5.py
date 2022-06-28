import numpy as np
import pandas as pd

# 指定のインデックスとカラムを持つDataFrameを乱数によって作成する関数です
def make_random_df(index, columns, seed):
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df

columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)

# df_data1とdf_data2を横方向に連結し、Keysに"X"、"Y"を指定してMultiIndexにしてdfに代入してください
df = pd.concat([df_data1, df_data2], axis=1, keys=["X", "Y"])

#  dfの"Y"ラベルの"banana"をY_bananaに代入してください
Y_banana = df["Y", "banana"]

print(df)
print()
print(Y_banana)