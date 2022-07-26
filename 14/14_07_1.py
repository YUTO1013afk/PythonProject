import math

func_list = [math.sqrt, math.exp, math.sin]
data_list = [0, 0.5, 1.0, 2]

for f in func_list:
    ans = list(map(f, data_list))
    print(ans)
