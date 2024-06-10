# sources: 
#   - https://www.datacamp.com/tutorial/python-numpy-tutorial
#   - https://numpy.org/doc/stable/user/absolute_beginners.html

import numpy as np 

a = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
a2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# a3 = np.array([[1,2,3,4], [1,2]]) # throws a ValueError, 
# since the array has an inhomogeneous shape

print(a)
print(a.shape)
print(a.dtype)
print(a.strides)
#print(a2)
#print(a2.shape)

# inspecting arrays
print(a.ndim)
print(a.size)
print(a.flags)
print(a.itemsize)
print(a.nbytes)

# Creating arrays
# array from list
np.array([1,2,3]) # array([1,2,3])
# array of ones
np.ones((2,3)) # 2x3 matrix filled with ones

# array of zeros and empty array
np.zeros(2, dtype=np.int64) # array([0, 0])
np.empty(2) # array([0., 0.])

# array with used-defined value
np.full((2,2), 3) # 2x2 matrix filled with 3's

# array with random values
np.random.random((2,2)) # 2x2 matrix filled with random values [0,1]
# array with a range of elements
np.arange(4) # array([0, 1, 2, 3])

# array with range of evenly spaced intervals
# np.arange(<first_number>, <last_number>, <step_size>)
np.arange(2,9,2) # array([2, 4, 6, 8])

# use np.linspace() to create an array with values spaced linearly in a specified inteval
np.linspace(0, 10, num=5) # array([ 0. ,  2.5,  5. ,  7.5, 10. ])

# identity matrix
np.eye(3) # 3x3 identity matrix

# array with random values
np.random.random((2,2)) # 2x2 matrix filled with random values between 0 and 1

###
# Array Attributes
a4 = np.array([[1,2,3], [3,4,5]])
print("shape:", a4.shape)
print("ndim:", a4.ndim)
print("size:", a4.size)
print("dtype:", a4.dtype)
print("itemsize:", a4.itemsize)
print("nbytes:", a4.nbytes, "= size * itemsize =", a4.size, "*", a4.itemsize)