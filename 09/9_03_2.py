import pandas as pd

dict1 = {"Sun": 6, "Mon": 7, "Tue": 6, "Wed": 5, "Thu": 9, "Fri": 6, "Sat": 8}
series1 = pd.Series(dict1)

print(series1)
print(series1.index)
print(series1.values)
print(series1[6])
print(series1["Wed"])
