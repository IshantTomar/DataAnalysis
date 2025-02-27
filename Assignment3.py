import numpy as np
# # Finding the k smallest values of a NumPy array
# arr = np.array([23,2,3,4,5,6,7])
# print(np.min(arr))

# # How to get the n-largest values of an array using NumPy?
# arr = np.array([23,2,3,4,5,6,7])
# sorted_index = np.argsort(arr)      #returns stored indexes
# sorted_array = arr[sorted_index]
# n = 2
# n_largest = sorted_array[-n: ]
# print(n_largest)

# # Sort the values in a matrix
# mat = np.matrix('[23,2;3,4]')
# mat.sort()
# print(mat)

# # Multiply 2d numpy array corresponding to 1d array
# arr1 = np.array([[1,2,3], [4,5,6]])
# arr2 = np.array([8,9,10])
# print(arr1*arr2)

# # Computes the inner product of two arrays
# arr1 = np.array([[1,2,3], [4,5,6]])
# arr2 = np.array([[8,9,10], [11,12,13]])
# print(np.inner(arr1, arr2))

# # Compute the nth percentile of the NumPy array

# # Calculate the n-th order discrete difference along the given axis

# # Calculate the sum of all columns in a 2D NumPy array
# arr_2d = np.array([[1,2,3], [4,5,6],
#                    [8,9,10], [11,12,13]])
#
# for i in range(0, len(arr_2d[0])):
#     add = 0
#     for j in range(0, len(arr_2d)):
#         add += arr_2d[j][i]
#     print(add)