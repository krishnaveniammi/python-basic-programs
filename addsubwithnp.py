import numpy as np   # Import NumPy library

# Taking input for matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input for first matrix
print("\nEnter elements of first matrix row by row:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input for second matrix
print("\nEnter elements of second matrix row by row:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Convert lists to numpy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

print("\nFirst Matrix:\n", matrix1)
print("\nSecond Matrix:\n", matrix2)

# Matrix Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:\n", addition)

# Matrix Subtraction
subtraction = matrix1 - matrix2
print("\nMatrix Subtraction:\n", subtraction)

# Matrix Multiplication (dot product)
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:\n", multiplication)

# Transpose of matrices
transpose1 = matrix1.T
transpose2 = matrix2.T
print("\nTranspose of First Matrix:\n", transpose1)
print("\nTranspose of Second Matrix:\n", transpose2)
