import numpy as np

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
# print(array_1d)

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
# print(array_2d)

# Element-wise addition
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
result = array_1 + array_2
# print(result)  # Output: [5 7 9]

# Element-wise multiplication
result = array_1 * array_2
# print(result)  # Output: [ 4 10 18]

# Array Indexing and Slicing
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing
# print(array[0, 1])  # Output: 2
# print(array[1:3, 2:3])
sliced_array = array[1:3, 2:3]

array_OneD = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(array_OneD[-1:-10:-1])

# Slicing
# print(array[0:2, 1:3])  # Output: [[2 3]
                          #        [5 6]]

# Creating arrays of zeros and ones
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))

# Creating an identity matrix
identity_matrix = np.eye(3)
# print("eye")

# Creating arrays with a range of values
array_range = np.arange(0, 10, 2)
# print (array_range)

# Creating arrays with values spaced linearly
linear_space = np.linspace(0, 1, 4)
# print(linear_space)

# Mathematical Functions
array = np.array([11, 2, 3, 4, 5])
print(array[0])


# Basic mathematical functions
sum_array = np.sum(array)
mean_array = np.mean(array)
std_array = np.std(array)
# print(sum_array)
# print(mean_array)
# print(std_array)

# Random numbers from a uniform distribution
random_uniform = np.random.rand(3, 3)
# print (random_uniform)
# Random numbers from a normal distribution
random_normal = np.random.randn(3, 3)
# print (random_normal)


# Linear Algebra Operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
product = np.dot(matrix_a, matrix_b)
print(product)

# Determinant
determinant = np.linalg.det(matrix_a)

# Inverse
inverse = np.linalg.inv(matrix_a)


array = np.arange(1, 13)  # Array with values from 1 to 12
reshaped_array = array.reshape(3, 4)  # Reshaping to 3x4 matrix
print(reshaped_array)


array = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2

# Broadcasting the scalar to each element of the array
result = array * scalar
print(result)
