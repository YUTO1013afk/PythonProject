import pandas as pd
import matplotlib.pyplot as plt

fig, axs = plt.subplots(5,5, figsize=(10, 10))
fig.subplots_adjust(wspace=0.56, hspace=1.3)

subject_df = pd.read_csv('test_score.csv')    # データセットの読み込み
df = pd.DataFrame(subject_df, columns=['国語', '数学', '英語', '理科', '社会'])

for i in range(5):
    for j in range(5):
        axs[i,j].scatter(df[subject_df.columns[i+3]], df[subject_df.columns[j+3]], s=8)
        axs[i,j].grid(True)  # グリッド線の表示
        axs[i,j].set_xlabel(df.columns[(i - i) + i], fontname="MS Gothic")  # X軸のラベル
        axs[i,j].set_ylabel(df.columns[j], fontname="MS Gothic")            # Y軸のラベル

plt.show() 