# 1. Create a 1-D NumPy array a of length = 4 containing random values between 0 and 100;
#    print it to the console
# 2. Create a 2-D NumPy array b containing the values [[1,2,3],[4,5,6],[7,8,9]]
#       - print the second element of the third row
#       - print the last two elements of the first two rows
#       - append a column of zeros to the array
# 3. Perform some mathematical operations on the arrays and print the results:
#       - compute the product of b and a
#       - compute the median of b
#       - create a new array containing the remainders of b divided by 3

import numpy as np

# 1.
a = np.random.random(4) * 100
print(a)

# 2.
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[2,1])
print(b[:2,-2:])
b = np.append(b, np.zeros((3,1), dtype=np.int64), axis=1)
print(b)

# 3.
b = np.multiply(b,a)
print(b)
print(np.median(b))
remainders = np.remainder(b, 3)
print(remainders)