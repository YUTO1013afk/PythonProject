import csv
FILENAME = 'titanic.csv'


df = []
with open(FILENAME) as f:
    line = csv.reader(f, delimiter=',', quotechar='"')
    for terms in line:
        df.append(terms)
print(df)
# これなら一応問題なく読み込める。
