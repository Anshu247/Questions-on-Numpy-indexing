import numpy as np

arr1 = np.array([1, 2, -3, 4, -5, -6, 7])
arr1[arr1 < 0] = 0

print(arr1)
# -------------------------------------------------------------

# using where method

# Python code to demonstrate
# to replace negative values with 0

ini_array1 = np.array([1, 2, -3, 4, -5, -6])

# printing initial arrays
print("initial array", ini_array1)

# code to replace all negative value with 0
result = np.where(ini_array1<0, 0, ini_array1)

# printing result
print("New resulting array: ", result)
# -------------------------------------------------------------

# using clip method

# Python code to demonstrate
# to replace negative values with 0

# supposing maxx value array can hold
maxx = 1000

ini_array1 = np.array([1, 2, -3, 4, -5, -6])

# printing initial arrays
print("initial array", ini_array1)

# code to replace all negative value with 0
result = np.clip(ini_array1, 0, 1000)

# printing result
print("New resulting array: ", result)

