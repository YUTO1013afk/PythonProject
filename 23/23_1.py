from sklearn.datasets import load_digits

digits = load_digits()
print(type(digits))
print(digits.keys())
for key in digits.keys():
    print('-='*30)
print('key=', key, ' value=', digits[key])
print(digits['data'].shape)