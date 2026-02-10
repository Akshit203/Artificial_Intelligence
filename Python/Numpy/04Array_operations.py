import numpy as np

# Array Operations :

arr = np.array([

               [ [1,2,3,4,5], [1,3,5,2,3] ],

               [ [2,3,8,0,3], [2,5,7,4,5] ],

               [ [4,5,6,7,8], [6,7,0,9,6] ]
               
               ])

print("Array : ", arr.shape)
print("Dimension :", arr.ndim)
print("Size :", arr.size)
print("DataType :", arr.dtype)


arr = np.arange(12)
print("Original array :", arr)

reshape = arr.reshape((4,3))
print("Reshaped Array :", reshape)

# Converts any n-D array into a 1-D array.
# flatten() returns a copy of the array converted into 1-D.

arr1 = np.array([[1,2,3],[4,5,6]])

flattened = arr1.flatten()
print("Flattend array :", flattened)
flattened[0] = 100
print("Original array ",arr1)

# ravel() returns a view of the array as 1-D (if possible).

arr2 = np.array([[9,8,7],[6,5,4]])
ravel = arr2.ravel()
print("ravel array :",ravel)

ravel[0] = 100
print("Original array :",arr2)  # [[100   8   7] [  6   5   4]] original array changed

# Transpose matrix
# row becomes coloumn & column becomes row

arr3 = np.array([[1,2,3], [4,5,6]])
transpose = arr3.T
print("Original Array :",arr3)
print("transpose Array :",transpose)

# array starting at 0 up to (but not including) 10, with a step of 2
# arange is like range(): step-based and usually excludes end,
# but with floats the end value is not guaranteed (rounding issues)

x = np.arange(0, 10, 2)
print(x)  # Output: [0 2 4 6 8]

# array of 5 evenly spaced numbers between 0 and 1 (inclusive)
y = np.linspace(0, 1, 5)
print(y)  # Output: [0.   0.25 0.5  0.75 1.  ]

# 4 x 4 identity matrix (1s on the diagonal, 0s elsewhere)
z = np.eye(3)
print(z)

# Array Slicing :

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print("Slicing :",arr[2:7]) 
# start - stop - step (stop non inclusive)

print("slicing with step :",arr[0:5:2])

print("Negative slicing :", arr[-3])

# 2d array slicing :

arr_2d = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print("Specific Element:", arr_2d[1,2]) #6
print("Entire row:", arr_2d[1]) # [4,5,6]
print("Entire coloumn:",arr_2d[:,2]) # [3,6,9]

# Sorting Array :

unsorted = np.array([1,0,3,7,3,0,9,2,5])
print("sorted array:",np.sort(unsorted))

arr_2d_unsorted = np.array([[8,1],
                            [4,2],
                            [2,0]])

# Default sort (axis=-1 by default, i.e., sort along last axis → row-wise)
# Each row is sorted individually
print("sorted:", np.sort(arr_2d_unsorted))

# Sorts elements "down each column"
print("column wise sorting", np.sort(arr_2d_unsorted, axis=0))

# Sorts elements "across each row"
print("row wise sorting:", np.sort(arr_2d_unsorted, axis=1))

# Filter 
num = np.array([1,2,3,4,5,6,7,8,9,10])

even = num[num%2 == 0] # NumPy allows boolean expressions directly inside [], 
                       # even = [n for n in num if n % 2 == 0]
                       # Without NumPy, we use a loop to pick even numbers
                       # NumPy lets us filter directly; plain Python needs more steps



print(even)

# filter with mask

num = np.array([1,2,3,4,5,6,7,8])
mask = num % 2 == 0

print(num[mask]) # [2 4 6 8]


# np.where vs fancy indexing :

# np.where () Checks condition
# Checks condition
# Returns a new array based on true/false values

# np.where(condition, value_if_true, value_if_false)


arr = np.array([10, 5, 20, 8])

result = np.where(arr > 10, 1, 0)
print(result) # [0 0 1 0]

# Fancy Indexing — Index-Based Selection

arr = np.array([10, 5, 20, 8])

indices = [0, 2]
print(arr[indices]) # [10 20]

# Adding removing data

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

combined_arr = np.concatenate((arr1,arr2))
print(combined_arr) # [1 2 3 4 5 6 7 8]

# array compatability 

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])

print("compatabilty shapes :", a.shape == b.shape) # True

# vstack vs hstack

original_arr = np.array([[1,2],
                         [3,4],
                         [5,6]])
new_row = np.array([1,1])

x = np.vstack((original_arr, new_row))
print(x)

new_row2 = np.array([[1],[1],[1]])
y = np.hstack((original_arr, new_row2))
print(y)
