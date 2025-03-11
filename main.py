import numpy as np
# arr = np.array([
#     [1,2,3,4],
#     ['a','b','c','d']])
# print(arr[0:2, ::-1])
#
# arr = np.array([[1,2,3], [4,5,6]])
# print(arr)
# print(np.transpose(arr))

# lap = np.random.laplace(7.2, 1, 35)
# print(round(np.mean(lap),2))
# print(round(np.var(lap),2))

# uniform_data = np.random.uniform(1,3,(4,3))
# print(uniform_data)

# n1 = np.array([10,20,30,40,10])
# n2 = np.array([30,60,10,80,'q','w', 10])
# print(np.intersect1d(n1, n2, assume_unique=True))
# print(np.setdiff1d(n2, n1))

# print(n1 + 2)
# pull test
# print(np.argmin(n1))
# print(np.argmax(n1))

# print(np.mean(n1))
# print(np.median(n1))
# print(sum(n1))
# more test

# arr_2d = np.array([[1,2,3], [4,5,6]])
# print(np.diff(arr_2d, axis=0)) #--> [[3 3 3]]
# print(np.diff(arr_2d, axis=1)) #--> [[1 1]
#                                   #    [1 1]]
import nbformat
import json

# Replace 'path/to/your/notebook.ipynb' with the actual path to your notebook
with open('./Netflix_dataset.ipynb', 'r') as f:
    notebook = json.load(f)

# Count the number of cells
cell_count = len(notebook['cells'])
print(f"The notebook has {cell_count} cells.")