import numpy as np

arr1 = np.array([77, 24, 90, 66, 100, 35, 20])
arr2 = np.array([[77, 24, 90, 66], [100, 35, 20, 10]])

arr1[arr1 > 50] = 1
arr2[arr2 < 50] = 1

print(arr1)
print(arr2)