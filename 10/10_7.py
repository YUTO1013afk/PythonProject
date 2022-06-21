import pandas as pd

df = pd.read_excel('fruits.xlsx')

print(df)
print()

# 練習1 10_2.py の処理
df2 = pd.DataFrame([df['fruits'],df['year'],df['time']])
print(df2)
print()

# 以下別解
df = df.loc[range(0,5), ["fruits", "year", "time"]]
df = df.T
print(df)

df = df.iloc[range(0,5), [0,2,1]]
df = df.T
print(df)