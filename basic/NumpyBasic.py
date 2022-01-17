import numpy as np

arr1D = np.array((1,2,3,4,5))

#create numpy
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Shape: ", arr3D.shape,"Type: ", type(arr3D), "Dimensions: ", arr3D.ndim)

#Create 5 dimension
arr5D = np.array([1,2,3,4,5], ndmin = 5)
print(arr5D)

#array start:end:step
print(arr1D[1:5:2])

#specify datatype
#i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

arr1D = np.array([1,2,3,4,5], dtype='S')
print(arr1D, arr1D.dtype)

#change datatype
arr1D = arr1D.astype(int)
print(arr1D, arr1D.dtype)

#copy and view a array
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
arr[0] = 9

print(x)
print(y)

#Reshape array

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#Iterator array and convert number to string

for x in np.nditer(arr3D,flags=['buffered'], op_dtypes=['S']):
    print(x)

#Iterator array with step

for x in np.nditer(arr3D[:,:,::2]):
    print(x)

#Iterator with index

for idx, x in np.ndenumerate(arr3D):
    print(idx, x)

#stack vs concatenate

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arrConcatenate = np.concatenate((arr1, arr2), axis = 1)
arrStack = np.stack((arr1, arr2), axis = 1)

print(arrConcatenate)
print(arrStack)

#array_split with array 1D

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 7)
print(newarr)

#array_split with array 2D

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

#array_split same with stack: axis, vsplit, hsplit, dsplit

#search array

arr = np.array([1,2,3,4,5,6,5,4,2])
print(np.where(arr == 4))

#sort

print(np.sort(np.array([[3, 2, 4], [5, 0, 1]])))

#filter

arr = np.array([41, 42, 43, 44])
x = arr[[True, False, True, False]]
print(x)