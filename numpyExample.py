import array

from numpy import *



# 6 Ways to create array by numpy
# 1. array()
# 2. linspace()
# 3. logspace()
# 4. arange()
# 5. zeros()
# 6. ones()

# 1. Create basic array by using numpy
# arr = array([1,23,4,5],int)
# print(arr)
# print(arr.dtype)


# 2. linspace
# arr=linspace(0,15,2)
# print(arr)

# 3. arange
# arr=arange(1,15,3)
# print(arr)

# 4. logspace
# arr=logspace(1,40,5)
# # (10^1+10^40)/5
# print(arr)

# .............numpy other function
arr=array([1,2,3,4,5])
print(arr)

# add 5 in each element
# for i in range(len(arr)):
#     arr[i]+=5
# print(arr)

# add 5 in each element using function
# arr=arr+5
# print(arr)

arr2=array([2,3,4,5,6])
print(arr2)

# # add to array
# arr3=arr+arr2
# print(arr3)


# find the sin ,cos , log,sqrt,min,max,sort of arra
print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(sort(arr))

# copy an array
arr1=array([2,4,6,8])
# arr2=arr1
# # same memory address (shallow copy)
# print(id(arr1))
# print(id(arr2))
# arr2[0]=3
# print(arr1)
# print(arr2)

# view create a new array in different fun
# arr2=arr1.view()
# print(id(arr1))
# print(id(arr2))

# to make deep copy or copy one array into second
# witout same memory addres
arr2=arr1.copy()
arr2[0]=3
print(arr1)
print(arr2)




