from sklearn.datasets import load_iris
iris = load_iris()
print(type(iris))
print(iris.keys())
for key in iris.keys():
    print('-='*30)
    print('key=', key, ' value=', iris[key])
print(iris['data'].shape)