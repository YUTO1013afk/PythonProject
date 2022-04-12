import sys
def py2_or_py3():
    #インデントが1段下がっているので関数内部
    major = sys.version_info.major
    if major < 3:
        # さらにインデントが下がっているので、if内部
        return 'Python 2'
    else:
        # else内部
        return 'Pyhton 3'

# 関数の呼出実⾏
py2_or_py3()
