A = 123
B = 45
M = 29989
x = 0
loop = 60000

result = dict.fromkeys(range(1, 7), 0)
# result = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(loop):
    x = (A * x + B) % M
    rand = x / (M-1) #0-1に正規化
    # print(rand)
    dice = int(rand * 6) + 1
    # print(dice)
    result[dice] += 1

print(result)