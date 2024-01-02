

# read data from file
# f=open('test.txt','r')
#
# print(f.readline(4),end="")
# print(f.readline())

# #write into a file
# f1=open('abc','w')
# f1.write("something")
# f1.write(" People")

# append into a file
# f1=open('abc','a')
# f1.write("mobile")

# read data from one file and write into another
f=open('test.txt','r')
f1=open('abc','w')

for data in f:
    f1.write(data)
