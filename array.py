# import array as arr
from array import *

# b=signed char
# B=unsigned char
# u=Py_UNICODE
# h=signed short
# H= unsigned short
# i=signed int
# I = unsigned int
# l=signed long
# L=unsigned long
# f=float
# d=double


val = array('i', [5, 9, 8, 2])
# print(val)

# print(val.buffer_info()) # give size of array
#
# print(val.typecode) # i
# val.reverse() #revese an array

n=len(val)
# print(n)
# print(val)

# for i in range(n):
#     print(val[i],"  ",end="")

# for e in val:
#     print(e)

# creating a new array using previous one
# newArr= array(val.typecode,(a for a in val))
# print(newArr)


arr=array('i',[])
lenUserArray=int(input("Enter the length of the arr"))

for i in range(lenUserArray):
    x=int(input("Enter the next value\n"))
    arr.append(x)

print(arr)

searchVal=int(input("Enter a val to search\n"))

k=0
for e in arr:
    if e==searchVal:
        print(k)
    k+=1




