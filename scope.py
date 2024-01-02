#global variable
a=10

# def something():
#     # local variable
#     # a=14
#     # b=8
#
#     # if i want to use global var
#     global a
#     a=15
#
#     print(a)
#
# something()
# print(a)


# i want to use global and local both variable

a=10
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    print("in fun ",a)
    globals()['a']=15

something()
print(a)