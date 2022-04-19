import pprint

#九九表リストの定義
kuku = []

for i in range(1, 10):

    #列リストの定義・初期化
    row = []

    #計算処理
    for j in range(1, 10):
        row.append(i * j)
    kuku.append(row)

#九九表の表示
pprint.pprint(kuku)