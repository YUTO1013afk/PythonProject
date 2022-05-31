import numpy as np
from sqlalchemy import false

arr = np. array([1, 2, 3, 4])

print(arr[[3, 2, 0]])
print(arr[[True, False, True, False]])
