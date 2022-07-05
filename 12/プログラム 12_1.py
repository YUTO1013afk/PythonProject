import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi,)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

xlabels = ["90°", "180°", "270°", "360°"]
xpositions = [np.pi/2, np.pi, np.pi*3/2, np.pi*2]

ylabels = ["-1", "-0.5", "0", "0.5", "1"]
ypositions = [-1, -0.5, 0, 0.5, 1]

# グラフのタイトルを設定します
plt.title("graphs of trigonometric functions")

# グラフのx軸とy軸に名前を設定する
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# グラフにグリットを表示します
plt.grid(True)

# グラフのx軸にラベルを設定する
plt.xticks(xpositions, xlabels)
plt.yticks(ypositions, ylabels)

# データx、y1をグラフにプロットし、赤で表示
plt.plot(x, y1, color="r", label="y=sin(x)")

# データx、y2をグラフにプロットし、青で表示
plt.plot(x, y2, color="b", label="y=cos(x)")

# データx、y3をグラフにプロットし、緑で表示
plt.plot(x, y3, color="g", label="y=tan(x)")

plt.legend(["y=sin(x)", "y=cos(x)", "y=tan(x)"])

plt.ylim(-1.2, 1.2)

plt.show()