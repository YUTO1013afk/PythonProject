import pandas as pd

dataframe = pd.read_excel('titanic.xlsx')

print(dataframe.shape)
print(dataframe.shape[0])
print(dataframe.shape[1])
print(dataframe.columns)
print(dataframe.index)