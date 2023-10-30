# Python code to demonstrate
# to replace nan values
# with an average of columns

import numpy as np

# Initialising numpy array
ini_array = np.array([[1.3, 2.5, 3.6, np.nan],
					[2.6, 3.3, np.nan, 5.5],
					[2.1, 3.2, 5.4, 6.5]])

# printing initial array
print ("initial array", ini_array)

# column mean
col_mean = np.nanmean(ini_array, axis = 0)

# printing column mean
print ("columns mean", str(col_mean))

# find indices where nan value is present
inds = np.where(np.isnan(ini_array))

# replace inds with avg of column
ini_array[inds] = np.take(col_mean, inds[1])

# printing final array
print ("final array", ini_array)

#--------------ALTERNATE METHOD-------------------#

import numpy as np

# Create an example array with NaN values
array = np.array([[1.0, 2.0, np.nan],
                  [4.0, np.nan, 6.0],
                  [7.0, 8.0, 9.0]])

# Calculate the column means, ignoring NaN values
column_means = np.nanmean(array, axis=0)

# Find the indices of NaN values
nan_indices = np.isnan(array)

# Replace NaN values with column means using fancy indexing
array[nan_indices] = np.take(column_means, np.where(nan_indices)[1])

# Print the array with NaN values replaced
print(array)
