import pandas as pd
df = pd.read_excel('fruits.xlsx')

print(df)
print()

series = pd.Series({"fruits":"mango", "year":2008, "time":7})
df = df.append(series, ignore_index=True)
print(df)