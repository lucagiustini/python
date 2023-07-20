# import numpy library
import numpy as np

# create an array with numpy library
array = np.array([1, 2, 3, 4, 5])
# print the first element of the array
print(array[0])

# create a string array with numpy library
array = np.array(["a", "b", "c", "d", "e"])
# print the second element of the array
print(array[1])

# create a 2D array with numpy library
array = np.array([[1, 2, 3], [4, 5, 6]])
# print the first raw of the array
print(array[0])
# print the second element of the first raw of the array
print(array[0][1])
# print the second column of the array
print(array[:, 1])

# create a 3D array with numpy library
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print the array with all the elements
print(array)

# create a matrix with numpy library and print it
matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# print the size of the matrix and the array
print(matrix.size)
print(array.size)

# print the memory size of the matrix and the array
print(matrix.nbytes)
print(array.nbytes)

# create a 3D array with numpy library and print it using full method
array = np.full((3, 3), 5)
print(array)
array = np.zeros([3, 3])
print(array)