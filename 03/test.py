var_global = 100
def func():
    print(var_global)
    var_local = 'A' # var_global = 'A' はどうなる？
    # var_global = 'A'
    print(var_local)
print(var_global)
func()
# print(var_local)