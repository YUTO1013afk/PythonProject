import pandas as pd

df = pd.read_excel('fruits.xlsx')

print(df)
print()

df = df.loc[[2,3],["year","fruits"]]
print(df)
# df.iloc[2,3], [2,0]