import seaborn as sns

list = []
species = ['setosa', 'versicolor', 'virginica']
df = sns.load_dataset('iris')
# リストにspecies列の値を代入する
for iris in df['species']:
    list.append(iris)
# リストから欲しい値をカウントする
for key in species:
    val = list.count(key)
    print(f'{key} :{val}')