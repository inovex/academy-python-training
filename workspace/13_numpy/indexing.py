import numpy as np

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# indexing
print(a[1]) # select the second row
print(a[0][2]) # select the third element of the first row
print(a[0,2]) # select the third element of the first row

# slicing
print(a[:2]) # select all elements from the first two rows
print(a[:, 3]) # select the 4th element in each row
print(a[1:,:2]) # select the first 2 elements from all rows except the first

# slicing with conditions
print("slicing with conditions")
print(a[a > 8]) # items greater than 8
print(a[(a > 3) & (a < 10)]) # items greater than 3 AND smaller than 10
print((a <= 5) | (a > 10)) # matrix with boolean values based on condition
print(np.nonzero(a < 4)) # select indices from an array