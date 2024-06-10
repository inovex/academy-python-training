# source: https://www.datacamp.com/tutorial/python-numpy-tutorial
import numpy as np
x = np.array([[1,2,3], [3,4,5]])
y = np.array([6,7,8])

# adding x and y
print(np.add(x,y)) # [[7 9 11] [9 11 13]]
# subtracting arrays
print(np.subtract(x,y)) # [[-5 -5 -5] [-3 -3 -3]]
# multiply x and y
print(np.multiply(x,y)) # [[6 14 24] [18 28 40]]
# divide x and y
print(np.divide(x,y)) # (rounded) [[0.17 0.29 0.375] [0.5 0.57 0.63]]

# sum of x
print(np.sum(x))

## aggregate functions
# array-wise sum
print(x.sum()) # 18
# array-wise min/max value, min/max of an array row
print(x.min(), x.max(), x.min(axis=1), x.max(axis=1)) # 1 5 [1 3] [3 5]
# cumulative sum of elements
print(x.cumsum(axis=1)) # [[1 3 6] [3 7 12]]
# mean and median
print(x.mean(), np.median(x)) # 3.0 3.0

# correlation coeff
print(np.corrcoef(x))
# standard deviation
print(np.std(x))