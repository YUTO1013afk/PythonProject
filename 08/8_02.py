FILENAME = 'titanic.csv'

df = []
with open(FILENAME) as f:
    for line in f:
        line = line.strip()
        df.append(list(line.split(',')))

print(df)
# 単純にカンマで区切ると上手くいかない…名前の項目にカンマが含まれている
