import pandas as pd
df = pd.read_excel('fruits.xlsx')

print(df)
print()

# 列の追加
df["price"] = [150, 120, 100, 300, 150]
print(df)