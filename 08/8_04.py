import pandas as pd

dataframe = pd.read_csv('titanic.csv')

print(dataframe)

dataframe = pd.read_excel('titanic.xlsx')

print(dataframe)
# print(dataframe.info)
