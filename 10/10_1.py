import pandas as pd

df = pd.read_excel('fruits.xlsx')
print(df)
print()
print(df.index)
print()
print(df.values)
print(type(df.values))
print()
print(df.columns)
