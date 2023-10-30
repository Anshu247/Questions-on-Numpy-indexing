import numpy as np

# Code 1
arr1 = np.array([1, 7, 0, 0, 2, 4, 6, 0, 9, 3, 0])
res = np.where(arr1 == 0)[0]

print(res)

# Code 2

# creating a 3-D Numpy array
n_array = np.array([[0, 2, 3],
					[4, 1, 0],
					[0, 0, 2]])

print("Original array:")
print(n_array)

# finding indices of null elements
# using np.argwhere()
print("\nIndices of null elements:")
res = np.argwhere(n_array == 0)

print(res)
