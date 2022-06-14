import pandas as pd
import sys
import platform
import numpy as np

# pythonのバージョン
print(sys.version)
print(platform.python_version())
print('-'*20)

# ライブラリのバージョン
print(np.__version__)
print(pd.__version__)
print('-'*20)

# 依存パッケージの各バージョン
# pd.show_versions()
