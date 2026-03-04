# Perform the following operations using Numpy:
# a) Construct a Python program using NumPy to generate a 4x4 identity matrix.
# b) Develop a Python program to generate two 3x3 matrices filled with random integers (1 to 9), then perform matrix addition and matrix multiplication..

import numpy as np

# (a) Generate 4x4 Identity Matrix
identity_matrix = np.identity(4)
print("4x4 Identity Matrix:")
print(identity_matrix)

# (b) Generate two 3x3 random matrices
A = np.random.randint(1, 10, (3,3))
B = np.random.randint(1, 10, (3,3))

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
addition = A + B
print("\nMatrix Addition:")
print(addition)

# Matrix Multiplication
multiplication = np.dot(A, B)
print("\nMatrix Multiplication:")
print(multiplication)
