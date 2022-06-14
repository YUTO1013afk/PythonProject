import pandas as pd

list1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
series1 = pd.Series(list1)

print(series1)
print(series1.index)
print(series1.values)
print(series1[6])
