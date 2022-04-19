import math
print(" x sin(x) cos(x) tan(x)")

x = 0
for n in range(7):
    radian_angle = math.radians(x)
    print(f'{x:02}' + " ", end="")
    print(f'{math.sin(radian_angle):.4f} {math.cos(radian_angle):.4f} {math.tan(radian_angle):.4f}')
    x = x + 15