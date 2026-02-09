import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))

zeros = np.zeros([4,6])
print(zeros)

ones = np.ones([4,6])
print(ones)

custom_num = np.full((4,4), 2)
print(custom_num)

# random is not a method , random is a class in which different methods are present

# np.rand() method
random_num = np.random.rand()
print("random value :", random_num)

# np.random.randint(low, high = None, size = None)
# Parameters explained simply: low → starting value (inclusive), high → ending value (exclusive)
# size → shape of output array (can be int or tuple)
# size is NOT list, dict, set
# It is only: int → 1D array [OR] tuple → multi-dimensional array

random = np.random.randint(4, 7)
print("random value :", random)

random = np.random.randint(4, 7, (2,2))
print("random value : \n", random)

x = np.random.uniform(10, 20, size=5) # Random floats between custom range
print(x) # [14.24580705 19.62736928 18.62548625 11.86031137 10.65218971]

# Randomly picks element(s) from array/list
y = np.random.choice([10, 20, 30, 40])
y2 = np.random.choice([1, 2, 3, 4], size=2, replace=False)

print(y)
print(y2) # Randomly selects 2 elements
          # From the list [1, 2, 3, 4]
          # Without replacement (no duplicate values)

# sequence 
sequence = np.arange(0, 10, 2)
print(sequence)
