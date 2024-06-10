import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

# # transposing / reshaping
print(a)
print("---- reshape / transpose ----")
print(np.transpose(a))
print(a.shape)
# print(a.reshape(4, 2)) # same effect as np.transpose(a)
print(a.reshape(8)) # convert a into a 1-D array
# print(a.flattern()) # flattens the array into a 1-D array

# transposing a 1D array
a2 = np.array([1,2,3])
print(np.transpose(a2))

# flattening
print("---- flattening ----")
a_flatten = a.flatten() # [1,2,3,4,5,6,7,8]
print(a_flatten)
a_flatten[0] = 50 # does not affect parent array
print(a_flatten)
print(a) # changes to the new array do not change the parrent array

a_ravel = a.ravel()
a_ravel[0] = 50 # the same item is affected in the parent array, too
print(a_ravel)
print(a)
# reversing an array
print("---- flipping ----")
a2 = np.array([1,2,3,4])
print(np.flip(a2)) # reverse the aray
print(np.flip(a)) # reverse the array in all rows and all columns
print(np.flip(a, axis=1)) # reverseonly columns
print(np.flip(a, axis=0)) # reverse only rows

# inserting and deleting elements
print("---- insert and delete ----")
a = np.array([1,2,3,4])
a = np.insert(a, 1, 99)
print(a) # [1 99 2 3 4]
a = np.delete(a, [1])
print(a) # [1 2 3 4]
# multiple dimensions
a2 = np.array([[1,2,3], [4,5,6]])
a2 = np.insert(a2, 1, 2, axis=1)
print(a2) # [[1 2 2 3] [4 2 5 6]]
# append
a2 = np.append(a2, [[7], [8]], axis=1)
print(a2) # [[1 2 2 3 7] [4 2 5 6 8]

# joining and splitting