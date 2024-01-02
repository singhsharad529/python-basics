from numpy import *

arr1=array([
            [1,2,3,6,2,9],
            [4,5,6,7,5,3]
            ])

print(arr1)
print(arr1.dtype)
print(arr1.ndim) #dimention
print(arr1.shape) # (no of row,no of column)
print(arr1.size) #row*col

arr2=arr1.flatten() #multi to single dimen
print(arr2)

arr3=arr1.reshape(2,2,3) # 3d arr
print(arr3)

#matrics
mat=matrix(arr1)
print(mat) # looks similiar but get more function for matrics

m=matrix('1 2 3 4;5 6 7 8')
print(m)

