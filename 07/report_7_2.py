A = [70,80,50,60,70,75,70,85]
B = [60,90,40,70,70,85,75,70]

#　Aの合計と平均
sumA = sum(A)
numA = len(A)
avgA = sumA / numA

#　Bの合計と平均
sumB = sum(B)
numB = len(B)
avgB = sumB / numB

# Aの分散と標準偏差を求める
mean_A = sum(A)/len(A)
dev_A = 0
for i in A:
    dev_A += (i-mean_A)**2
var_A = dev_A/len(A)
std_A = var_A**0.5

# Bの分散と標準偏差を求める
mean_B = sum(B)/len(B)
dev_B = 0
for i in B:
    dev_B += (i-mean_B)**2
var_B = dev_B/len(B)
std_B = var_B**0.5

print(f'A組')
print(f'合計：{sumA}')
print(f'平均：{avgA}')
print(f'分散：{var_A}')
print(f'標準偏差：{std_A}')
print()
print(f'B組')
print(f'合計：{sumB}')
print(f'平均：{avgB}')
print(f'分散：{var_B}')
print(f'標準偏差：{std_B}')