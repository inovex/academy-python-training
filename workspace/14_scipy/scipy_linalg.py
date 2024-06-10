# source: https://www.mygreatlearning.com/blog/scipy-tutorial/#scipy-linalg
import numpy as np
from scipy import linalg

### solve linear equations
# let's solve a linear algebra system given as
#       x  + 2y - 3z = -3
#       2x - 5y + 4z = 13
#       5x + 4y -  z = 5

# creating input array
x = np.array([[1, 2, -3], [2, -5, 4], [5, 4, -1]])
# creating the solution array
y = np.array([[-3], [13], [5]])
# solve the linear algebra system
res = linalg.solve(x, y)
print(res) # [[2.] [-1.] [1.]]
print(x.dot(res) - y) # [[0.] [0.] [0.]]

## finding a determinant of a square matrix
M = np.array([[1,2],[3,8]])
# computing the determinant
det = linalg.det(M)
print(det) # 2.0

## finding the inverse of a matrix
A = np.array([[1,3,5], [2,5,1], [2,3,8]])
B = linalg.inv(A)
print(A.dot(B))

## computing vector and matrix norms
A = np.array([[1,2], [3,4]])
print(A)
print(linalg.norm(A, ord=1)) # L1 norm (max column sum) -> 6.0
print(linalg.norm(A, ord='fro')) # frobenius norm (default) -> 5.477225575051661
print(linalg.norm(A, ord=np.inf)) # L inf norm (max row sum) -> 7.0

