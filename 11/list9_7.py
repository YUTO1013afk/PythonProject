import numpy as np
import pandas as pd

df1 = pd.read_csv('fruits_a.csv')
df2 = pd.read_csv('fruits_b.csv')

df3 = pd.merge(df1, df2, on="fruits", how="inner")

print(df3)
