import numpy as np

arr1 = np.array([[1, 2, np.nan], [4, 5, np.nan]])
res = arr1[:, ~np.isnan(arr1).any(axis = 0)]

print(res)

# Importing Numpy module
# import numpy as np

# # Creating 2X3 2-D Numpy array
# n_arr = np.array([[10.5, 22.5, np.nan],
# 				[41, 52.5, np.nan]])

# print("Given array:")
# print(n_arr)

# print("\nRemove all columns containing non-numeric elements ")
# print(n_arr[:, ~np.isnan(n_arr).any(axis=0)])
