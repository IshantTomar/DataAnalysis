import numpy as np
arr = np.array([23,2,3,4,5,6,7])
# print(np.min(arr))
print(arr[np.argsort(arr)][0:3])