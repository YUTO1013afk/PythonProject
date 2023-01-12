import numpy as np

def f(a):
    return ((a-1.0)*(a-1.0))
def df(a):
    return (2.0*(a-1.0))

a = float(np.random.randint(-500, 500)) / 10
alpha = 0.1
print(f'Value of a at step 00 is {a:.7}, Value of f(a) is {f(a):.7}')

for i in range(1,101):
    a = a - alpha * df(a)
    print(f'Value of a at step {i:02} is {a:.7}, Value of f(a) is {f(a):.7}')