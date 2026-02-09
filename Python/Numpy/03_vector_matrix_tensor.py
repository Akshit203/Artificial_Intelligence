import numpy as np 

# A vector is a 1-D array that contains a list of numbers.
vector = np.array([1,2,3,4,5,6,7])
print(vector)

# A vector is a 1-D array that contains a list of numbers.
matrix = np.array([[1,2,3,4],
                   [7,4,1,2]])
print(matrix)

# A tensor is a generalized form of vector and matrix, having more than 2 dimensions.
tensor = np.array([
    [[1,2,6,7], [2,3,4,5]],
    [[2,5,1,4], [9,8,3,0]]
    ])
print("Tensor :", tensor)

