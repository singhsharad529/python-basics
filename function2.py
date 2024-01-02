# def update(x):
#     x=8
#     print("x ",x)
#
# # pass by value
# a=10
# update(a)
# print("a ",a)

# but in list case it is different because
# list is mutable but int,string are not mutable


def person(name,age): #formal arguments
    print(name)
    print(age)

person('sharad',6) #actual argument
person(name='sharad',age=6) #by keyword


# keyword variable length arg
def personFun(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


personFun('sharad',age=23,city='noida',mob=9871750805)
