import pandas as pd

df = pd.read_excel('fruits.xlsx')

print(df)	# 念の為出力
print()

series = pd.Series(["mango", 2008, 7], index=["fruits", "year", "time"])
df = df.append(series, ignore_index=True)

print(df)
