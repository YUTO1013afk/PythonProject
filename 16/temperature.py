import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('raw_data.csv', encoding = 'UTF8')
data["hour"] = data['time'].str[:2]
df_temp = data.groupby(["date", "hour"], as_index=False).mean()
# print(df_temp)

X1 = df_temp[df_temp.date == '2022-09-26']['hour']
Y1 = df_temp[df_temp.date == '2022-09-26']['temperature']
X2 = df_temp[df_temp.date == '2022-09-27']['hour']
Y2 = df_temp[df_temp.date == '2022-09-27']['temperature']
X3 = df_temp[df_temp.date == '2022-09-28']['hour']
Y3 = df_temp[df_temp.date == '2022-09-28']['temperature']

plt.figure(figsize=(16, 5))
plt.plot(X1,Y1, label="9/26")
plt.plot(X2,Y2, label="9/27")
plt.plot(X3,Y3, label="9/28")

# グラフのタイトル
plt.title("Temperature in my living")
# X軸ラベルの名前
plt.xlabel("hour")
# Y軸ラベルの名前
plt.ylabel("temperature")
# グリッド線の表示
plt.grid()
# 凡例の表示
plt.legend()
# グラフの表示
plt.show()