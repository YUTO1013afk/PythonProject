import pandas as pd
df = pd.read_excel('fruits.xlsx')

df = pd.DataFrame(df).T
print(df)