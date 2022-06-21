import pandas as pd
df = pd.read_excel('fruits.xlsx')

print(df)
print()

df2 = pd.DataFrame([df['fruits'],df['year'],df['time']])
print(df2)
print()