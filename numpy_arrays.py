# importing the numpy library:
import numpy as np
import array as arr

# creating an array with numpy
# 1D array
# a1d=np.array([1,2,3,4,45])
# print(a1d)

 # 2D array:
# a2d=np.array([[1,2,3],[5,67,77],[22,33,44]])
# print(a2d)

# methods and operations in numpy arrarys:
# 1. basic array s information method:
# a=np.array([1,2,3,4,5,])

# ndim:
# print(a.ndim)
# print(a2d.ndim)

# shape:
# print(a2d.shape)

# size:
# print(a2d.size)

# dtype:
# print(a2d.dtype)


# 2. creating an array with numpy:
# ZEROS:
print(np.zeros(6))

# ONES:
print(np.ones(11))

# ARRANGE:
print(np.arange(1,11,1))
print(np.arange(0,11,3))
print(np.arange(1,11,5))
print(np.arange(0,111,11))

# linespace:
print(np.linspace(0,10,3))

# mathematical operations:
a=np.array([2,3,5,7,11])
list=[45,18,7,17,63]
print(a+6)
print(a-2)
print(a*5)
print(a/2)
print(a**2)
print(a//6)

# aggregate functions:

# sum:
print(np.sum(a))

# mean:
print(np.mean(a))
      
# max:
print(np.max(a))

# min:
print(np.min(a))

# median:
print(np.median(a))

# std:
print(np.std(a))

# cumprod:
print(np.cumprod(a))


# matrix operations:
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(mat1+mat2)
print(mat1**2)
print(mat1*mat2)

# dot:
print(np.dot(mat1,mat2))

# transpose:
print(np.transpose(mat1))
print(np.transpose(mat2))
