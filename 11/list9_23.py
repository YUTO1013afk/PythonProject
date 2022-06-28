import pandas as pd

# 一部の都道府県に関するDataFrameを作成します
prefecture_df = pd.read_csv('prefecture.csv')
# 出力します
print(prefecture_df)

# prefecture_dfを地域(Region)についてグループ化し、grouped_regionに代入してください
grouped_region = prefecture_df.groupby("Region")

# prefecture_dfに出てきた地域ごとの、面積(Area)と人口(Population)の平均をmean_dfに代入してください
mean_df = grouped_region.mean()

# 出力します
print(mean_df)