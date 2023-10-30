import numpy as np

# Code 1
arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
lst = [1, 3, 5, 7]
res = np.isin(arr1, lst)

print(res)

# Code 2
# using numpy.isin() method
gfg1 = np.array([[1, 3], [5, 7], [9, 11]])
lis = [1, 3, 11, 9]
gfg = np.isin(gfg1, lis)

print(gfg)
