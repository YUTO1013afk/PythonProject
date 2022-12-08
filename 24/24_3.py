import cv2

filename = "./tegaki.png"
# 画像ファイルの読み込み
img_bgr = cv2.imread(filename)

# グレースケールに変換
img_gry = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 28×28にリサイズ
img_28 = cv2.resize(img_gry, dsize=(28, 28), interpolation=cv2.INTER_LANCZOS4)

# 白:255 黒:0なので、反転させる
img = 255 - img_28

# とりあえず、人間に分かるように表示
for yy in range(0, len(img)):
    for xx in range(0, len(img[yy])):
        print("{:3}".format(img[yy][xx]), end='')
    print()